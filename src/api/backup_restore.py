from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..db.database import get_db
import os
import fastavro
from datetime import datetime
import logging


router = APIRouter()

def export_to_avro(table_name, db_session):
    """Export the data from a table to an AVRO file."""
    query = text(f"SELECT * FROM {table_name}")
    result = db_session.execute(query)
    records = [dict(row._mapping) for row in result]

    if not records:
        raise HTTPException(status_code=404, detail=f"No data found in table {table_name}")

    # Define the AVRO schema based on the first record's keys and types
    fields = []
    for col, val in records[0].items():
        avro_type = ["null"]
        if isinstance(val, int):
            avro_type.append("int")
        elif isinstance(val, float):
            avro_type.append("float")
        elif isinstance(val, bool):
            avro_type.append("boolean")
        elif isinstance(val, datetime):
            avro_type.append("string")
            # Convert datetime to string in all records
            for record in records:
                record[col] = record[col].isoformat() if record[col] else None
        else:
            avro_type.append("string")
        fields.append({"name": col, "type": avro_type})

    schema = {
        "doc": f"Schema for {table_name}",
        "name": table_name,
        "namespace": "example.avro",
        "type": "record",
        "fields": fields
    }

    avro_file_path = os.path.join(os.getcwd(), f"{table_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avro")
    with open(avro_file_path, 'wb') as out:
        fastavro.writer(out, schema, records)

    return avro_file_path


def import_from_avro(table_name, file_path, db_session):
    """Import the data from an AVRO file into a table."""
    with open(file_path, 'rb') as file:
        reader = fastavro.reader(file)
        records = [record for record in reader]

    if not records:
        raise HTTPException(status_code=404, detail=f"No data found in AVRO file for table {table_name}")

    for record in records:
        columns = ', '.join(record.keys())
        values = ', '.join([f":{col}" for col in record.keys()])
        query = text(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        db_session.execute(query, record)

    db_session.commit()

@router.post("/backup/")
def backup_db(db: Session = Depends(get_db)):
    try:
        table_names = ["employees", "departments", "jobs"]  # List all the tables you need to backup
        backup_files = [export_to_avro(table, db) for table in table_names]
        return {"message": "Backup successful", "files": backup_files}
    except Exception as e:
        logging.error(f"Error during backup: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/restore/")
def restore_db(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())

        table_name = file.filename.split('_')[0]
        import_from_avro(table_name, file_location, db)

        return {"message": "Restore successful"}
    except Exception as e:
        logging.error(f"Error during restore: {e}")
        raise HTTPException(status_code=500, detail=str(e))

