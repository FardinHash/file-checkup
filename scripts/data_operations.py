import pandas as pd
from pymongo import UpdateOne

def read_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")

def update_database(db, df):
    collection = db['files']

    operations = []
    for _, row in df.iterrows():
        query = row.to_dict()  # Use the entire row as the query for duplication check
        update = {"$set": row.to_dict()}
        operations.append(UpdateOne(query, update, upsert=True))

    if operations:
        collection.bulk_write(operations)

    print("Data checked and updated in the database")
