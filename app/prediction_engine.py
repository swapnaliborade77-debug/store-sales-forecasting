import numpy as np
import pandas as pd

def get_prediction(model, input_dict):
    # 1. Convert dictionary to DataFrame
    df = pd.DataFrame([input_dict])
    
    # 2. Ensure columns are in the EXACT order as training
    # Example order: ['Store', 'DayOfWeek', 'Promo', 'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment']
    feature_order = ['Store', 'DayOfWeek', 'Promo', 'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment']
    df = df[feature_order]
    
    # 3. Predict
    prediction = model.predict(df)
    
    # Return the result (Rossmann models often predict log(Sales), so use exp if needed)
    return max(0, prediction[0])