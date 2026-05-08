import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

def get_data_from_sql():
    user = "root"
    password = urllib.parse.quote_plus("Swapnali@2020")
    host = "localhost"
    db_name = "rossmann_sales_db"
    
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}")
    
    print("Fetching joined data from SQL...")
    # We join sales data with store metadata in one SQL query
    query = """
    SELECT t.*, s.StoreType, s.Assortment, s.CompetitionDistance
    FROM sales_train t
    JOIN store_info s ON t.Store = s.Store
    WHERE t.Open = 1;
    """
    df = pd.read_sql(query, con=engine)
    return df

def feature_engineering(df):
    print("Engineering features...")
    # 1. Handle Dates
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)
    
    # 2. Encode Categorical variables
    # StateHoliday: a=public, b=Easter, c=Christmas, 0=None
    df['StateHoliday'] = df['StateHoliday'].astype(str).map({'0':0, 'a':1, 'b':2, 'c':3})
    df['StoreType'] = df['StoreType'].map({'a':0, 'b':1, 'c':2, 'd':3})
    df['Assortment'] = df['Assortment'].map({'a':0, 'b':1, 'c':2})
    
    # 3. Fill missing competition distance with a high number
    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].max())
    
    # Drop columns we don't need for the model
    # We drop 'Customers' because we won't know customer count in the future
    cols_to_drop = ['Date', 'Customers', 'Open']
    df = df.drop(columns=cols_to_drop)
    
    return df

if __name__ == "__main__":
    raw_data = get_data_from_sql()
    processed_data = feature_engineering(raw_data)
    print(f"Data ready! Shape: {processed_data.shape}")
    processed_data.to_csv('data/processed_data.csv', index=False)