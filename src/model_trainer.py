import pandas as pd
import xgboost as xgb
import pickle
from sqlalchemy import create_engine
import urllib.parse
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import os

def train_sales_model():
    # 1. Database Connection
    user = "root"
    password = urllib.parse.quote_plus("Swapnali@2020")
    # Using pymysql as it proved stable in our tests
    engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost/rossmann_sales_db")

    print("Reading data from SQL for training...")
    # We join the two tables and filter for open stores with sales
    query = """
    SELECT t.Store, t.DayOfWeek, t.Promo, t.StateHoliday, t.SchoolHoliday, 
           t.Sales, s.StoreType, s.Assortment
    FROM sales_train t
    JOIN store_info s ON t.Store = s.Store
    WHERE t.Open = 1 AND t.Sales > 0
    LIMIT 200000; -- Using a large sample for training
    """
    df = pd.read_sql(query, con=engine)

    # 2. Preprocessing (Turning letters into numbers for the AI)
    print("Preprocessing data...")
    # Convert '0', 'a', 'b', 'c' to 0, 1, 2, 3
    df['StateHoliday'] = df['StateHoliday'].map({'0':0, 'a':1, 'b':2, 'c':3}).fillna(0)
    df['StoreType'] = df['StoreType'].map({'a':0, 'b':1, 'c':2, 'd':3})
    df['Assortment'] = df['Assortment'].map({'a':0, 'b':1, 'c':2})

    # 3. Split data into Features (X) and Target (y)
    X = df.drop('Sales', axis=1)
    y = df['Sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train the XGBoost Model
    print("Training XGBoost model (this may take a minute)...")
    model = xgb.XGBRegressor(
        objective='reg:squarederror', 
        n_estimators=100, 
        learning_rate=0.1, 
        max_depth=6
    )
    model.fit(X_train, y_train)

    # 5. Evaluate the model
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"✅ Training Complete! Average Error: €{rmse:.2f}")

    # 6. Create 'models' folder and save the file
    if not os.path.exists('models'):
        os.makedirs('models')
        
    with open('models/sales_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("✅ Model saved as models/sales_model.pkl")

if __name__ == "__main__":
    train_sales_model()