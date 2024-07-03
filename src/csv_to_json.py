import pandas as pd
import json
import logging

# Configurar el logging
logging.basicConfig(filename="data_conversion_errors.log", level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def handle_nan_values(data):
    """
    Reemplaza los valores NaN con None y registra los valores NaN.
    """
    for key, value in data.items():
        if pd.isna(value):
            logging.error(f"Invalid data in column '{key}': {value}")
            data[key] = None
    return data

def save_json(data, filename):
    """
    Guarda los datos en un archivo JSON.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def convert_csv_to_json():
    # Leer y procesar el archivo departments.csv
    departments_df = pd.read_csv('data/departments.csv', header=None, names=['id', 'name'])
    departments_json = departments_df.apply(handle_nan_values, axis=1).to_dict(orient='records')
    save_json(departments_json, 'data/departments.json')

    # Leer y procesar el archivo jobs.csv
    jobs_df = pd.read_csv('data/jobs.csv', header=None, names=['id', 'title'])
    jobs_json = jobs_df.apply(handle_nan_values, axis=1).to_dict(orient='records')
    save_json(jobs_json, 'data/jobs.json')

    # Leer y procesar el archivo hired_employees.csv
    employees_df = pd.read_csv('data/hired_employees.csv', header=None, names=['id', 'name', 'datetime', 'department_id', 'job_id'])
    employees_json = employees_df.apply(handle_nan_values, axis=1).to_dict(orient='records')
    save_json(employees_json, 'data/employees.json')

    # Crear el diccionario final
    combined_data = {
        "employees": employees_json,
        "departments": departments_json,
        "jobs": jobs_json
    }

    # Guardar el archivo JSON combinado
    save_json(combined_data, 'data/batch_data.json')

    print("CSV data successfully converted to JSON.")

if __name__ == "__main__":
    convert_csv_to_json()
