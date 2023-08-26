#importing libraries
import pandas as pd
import numpy as np
import uvicorn
from fastapi import FastAPI
import pickle
#from sklearn.model_selection import LogisticRegression
from variables import Clickad
import sklearn

#creating and initializing objecct
app=FastAPI()

#load model
# Load the saved model from the file
#with open(logmodel_filename, 'rb') as file:
    #logmodel = pickle.load(file)
pickle_in = open("logmodel.pkl","rb")
logmodel=pickle.load(pickle_in)





#index route
@app.get('/')
def index():
    return{'message':'Predicting if someone clicked on an ad'}

@app.get('/{name}')
def get_name(name:str):
    return{'message':f'Hello,{name}'}

#prediction functionality
@app.post('/predict')
def predict_ad(data:Clickad):
    data=data.dict()
    time=data['Daily_Time_Spent_on_Site']
    age=data['Age']
    income=data[ 'Area_Income']
    internet=data[ 'Daily_Internet_Usage']
    gender=data['Male']

    prediction=logmodel.predict([[time,age,income,internet,gender]])
    if (prediction[0] == 0):
        prediction= 'Not clicked the ad'
    else:
        prediction= 'Clicked the ad'
    return {
    'prediction':prediction
}


#running the app with uvicorn

if __name__ == '__main__':
      uvicorn.run(app, host='127.0.0.1',port= 8000)
