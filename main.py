from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app=FastAPI(
    title="water potability prediction",
    description="Predicting water Potability"
)

with open(r"model.pkl","rb") as f:
    model=pickle.load(f)

@app.get("/")
def index():
    return "welcome to water potability prediction fastapi"


@app.post("/predict")
def model_predict(water: Water):
    sample=pd.DataFrame({
        'ph': [water.ph],
    'Hardness' : [water.Hardness],
    'Solids' : [water.Solids],
    'Chloramines' : [water.Chloramines],
    'Sulfate' : [water.Sulfate ],
    'Conductivity' : [water.Conductivity],
    'Organic_carbon' : [water.Organic_carbon],
    'Trihalomethanes' : [water.Trihalomethanes],
    'Turbidity' : [water.Turbidity]
    })

    predicted_value=model.predict(sample)

    if predicted_value==1:
        return "water is consumable"
    else:
        return "water is not consumable"
    

