from typing import Union
from fastapi import FastAPI
from typing import List
import pandas as pd
import joblib
import json
from model import ChurnModel

modelRegression = joblib.load('../Models/LogisticRegression.joblib')
modelTree= joblib.load('../Models/DecisionTreeBest.joblib')


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/{model_version}/predict")
def predict_customer(model_version: float,  datas: List[ChurnModel]):
    pred=[]
    df = pd.DataFrame([data.dict() for data in datas])
    customer_ids = df['customerID'].tolist()

    if model_version == 1:
        predictions = modelTree.predict_proba(df)
        prediction_result = modelTree.predict(df)
        result = list(zip(customer_ids, predictions, prediction_result))
        result_dict_list = [
            {
                "customerID": customer_id,
                "Probabilidad_Churn_No": round(prediction[0], 3),
                "Probabilidad_Churn_Yes": round(prediction[1], 3),
                "Result": result  # Corregido aquí, asumiendo que 'result' es lo que deseas incluir
            } for customer_id, prediction, result in result
        ]
    elif model_version == 2:
        predictions = modelRegression.predict_proba(df)
        prediction_result = modelRegression.predict(df)
        result = list(zip(customer_ids, predictions, prediction_result))
        result_dict_list = [
            {
                "customerID": customer_id,
                "Probabilidad_Churn_No": round(prediction[0], 3),
                "Probabilidad_Churn_Yes": round(prediction[1], 3),
                "Result": result  # Corregido aquí, asumiendo que 'result' es lo que deseas incluir
            } for customer_id, prediction, result in result
        ]
    else:
        result_dict_list = "Modelo no definido, solo 1 y 2"

    return result_dict_list