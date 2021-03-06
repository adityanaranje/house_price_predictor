# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:12:13 2021

@author: ADITYA NARANJE
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("house.html")

#prediction function
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1,17)
    loaded_model = pickle.load(open("price_flask.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

#Output page
@app.route('/result', methods = ["POST"])
def result():
    if request.method =="POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float,to_predict_list))
        result = round(ValuePredictor(to_predict_list),2)
        return render_template("result.html",prediction= result)
    
#Main function
if __name__=="__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AUTO_RELODE"]=True