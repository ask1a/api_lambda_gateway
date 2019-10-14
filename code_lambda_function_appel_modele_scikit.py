import json
import pandas as pd
import joblib

model = joblib.load('/opt/house_price_model.pkl')

def lambda_handler(event, context):
        
    df = pd.DataFrame([event])
    
    # Returning the value from the list
    result = model.predict(df)[0] 
    
    return result
