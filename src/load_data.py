# src/load_data.py

import pandas as pd
import logging
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from .db.database import SessionLocal
from .db.models import Department, Job, Employee
from .db.init_db import init_db  # Importing for create tables if does not exist

# Configure logging to capture errors during data loading, storing them in "data_errors.log" with a specific format.
logging.basicConfig(filename="data_errors.log", level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def load_data():
    """
    Load data from CSV files into the database.
    This function reads data from departments.csv, jobs.csv, and hired_employees.csv,
    and inserts the data into the corresponding database tables.
    """
    
    # Create a new session
    session = SessionLocal()

    # Load and insert data into the Department table
    departments_df = pd.read_csv('data/departments.csv', header=None, names=['id', 'name'])
    for _, row in departments_df.iterrows():
        if pd.isna(row['id']) or pd.isna(row['name']):
            logging.error(f"Invalid row in departments data: {row.to_dict()}")  # Logging invalid rows
            continue
        stmt = insert(Department).values(id=row['id'], name=row['name'])
        stmt = stmt.on_conflict_do_nothing(index_elements=['id'])  # Avoid duplicate entries based on the 'id' column
        session.execute(stmt)

    # Load and insert data into the Job table
    jobs_df = pd.read_csv('data/jobs.csv', header=None, names=['id', 'title'])
    for _, row in jobs_df.iterrows():
        if pd.isna(row['id']) or pd.isna(row['title']):
            logging.error(f"Invalid row in jobs data: {row.to_dict()}")  # Logging invalid rows
            continue
        stmt = insert(Job).values(id=row['id'], title=row['title'])
        stmt = stmt.on_conflict_do_nothing(index_elements=['id'])  # Avoid duplicate entries based on the 'id' column
        session.execute(stmt)

    # Load and insert data into the Employee table
    employees_df = pd.read_csv('data/hired_employees.csv', header=None, names=['id', 'name', 'datetime', 'department_id', 'job_id'])
    for _, row in employees_df.iterrows():
        # Check for NaN values in mandatory columns
        if pd.isna(row['id']) or pd.isna(row['name']) or pd.isna(row['datetime']) or pd.isna(row['department_id']) or pd.isna(row['job_id']):
            logging.error(f"Invalid row in employees data: {row.to_dict()}")
            continue
        
        try:
            stmt = insert(Employee).values(
                id=row['id'], 
                name=row['name'], 
                datetime=row['datetime'], 
                department_id=row['department_id'], 
                job_id=row['job_id']
            )
            stmt = stmt.on_conflict_do_nothing(index_elements=['id'])  # Avoid duplicate entries based on the 'id' column
            session.execute(stmt)
        except ValueError as e:
            # Log any ValueError encountered during data processing
            logging.error(f"Error processing row: {row.to_dict()}, Error: {str(e)}")
            continue

    # Commit the session to save all changes to the database
    session.commit()
    # Close the session
    session.close()
    print("Data loaded successfully")

if __name__ == "__main__":
    init_db()  # creating tables if they do not exist
    load_data()  # loading data
