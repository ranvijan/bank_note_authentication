# Importing essential libraries
from flask import Flask, request

import pandas as pd
import numpy as np

import pickle



app=Flask(__name__)

pickle_in=open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)
@app.route('/')
def welcome ():
  return "Welcome All"

@app.route('/predict')
def predict_note_authenthication():

 variance=request.args.get('variance')
 skewness=request.args.get('skewness')
 curtosis=request.args.get('curtosis')
 entropy=request.args.get('entropy')

 prediction=classifier.predict([[variance,skewness,curtosis,entropy]])

 return "the predicted value is"+ str(prediction)


if __name__ == '__main__':
  app.run()
