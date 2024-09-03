from db_connection import get_database
import pandas as pd

def download_data():
    db = get_database()
    collection = db['files']
    
    # Fetch all data from the collection
    data = list(collection.find({}, {'_id': False}))
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV or Excel
    df.to_csv('downloaded_data.csv', index=False)
    # Or to Excel
    # df.to_excel('downloaded_data.xlsx', index=False)

if __name__ == "__main__":
    download_data()
