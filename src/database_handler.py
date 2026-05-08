import pandas as pd
from sqlalchemy import create_engine, String  # Changed this line
import urllib.parse

def store_data_to_sql():
    user = "root"
    password = urllib.parse.quote_plus("Swapnali@2020")
    engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost/rossmann_sales_db")

    try:
        print("--- Step 1: Uploading Store Info ---")
        store_df = pd.read_csv('data/store.csv')
        store_df.to_sql('store_info', con=engine, if_exists='replace', index=False)
        print("✅ store_info uploaded.")

        print("--- Step 2: Uploading Sales Train ---")
        chunk_container = pd.read_csv('data/train.csv', chunksize=100000, low_memory=False)
        
        for i, chunk in enumerate(chunk_container):
            chunk['StateHoliday'] = chunk['StateHoliday'].astype(str)
            chunk['Date'] = pd.to_datetime(chunk['Date'])
            
            mode = 'replace' if i == 0 else 'append'
            
            # Use String(10) with a capital S
            chunk.to_sql(
                'sales_train', 
                con=engine, 
                if_exists=mode, 
                index=False,
                dtype={'StateHoliday': String(10)} 
            )
            
            print(f"✅ Uploaded batch {i+1} ({ (i+1)*100000 } rows)...")

        print("✅✅ ALL DATA SUCCESSFULLY STORED!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    store_data_to_sql()