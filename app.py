# Import Libraries
import os
import numpy as np
import pandas as pd
import sqlalchemy
import flask
from flask_cors import CORS
from flask import Flask, render_template, redirect, jsonify,request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import psycopg2
# import config as creds
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
from datetime import date


# create instance of Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

#Define database connection
# conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
#                   + " password=" + creds.PGPASSWORD

# print(conn_string)
# conn = psycopg2.connect(conn_string)
# print("Connected!")
  

# covid_df = pd.read_sql_query(
#                    ''' SELECT * FROM coviddata 
#                    ''' , conn)

#Routes 
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/ageRisk')
def ageRisk():
    return render_template("2age.html")

@app.route('/ourModel')
def ourModel():
    return render_template("3model.html")

@app.route('/riskCalculator')
def riskCalculator():
    return render_template("4risk_cal.html")

@app.route('/correlation')
def correlation():
    return render_template("5corr.html")

@app.route('/aboutUs')
def aboutUs():
    return render_template("6bio.html")

def predictRisk(age, hypertension, diabetes, cvd, copd, cancer, kidneydisease, fever, breath, cough, tachypnea, fatigue, diarrhea) -> []: 

    ### Initialize:
    # Intialize error = No
    error_flag = False
    predicted_result = None
    input = {"age":[age], "hypertension":[hypertension], "diabetes":[diabetes], \
                 "cvd":[cvd], "copd":[copd], "cancer":[cancer], \
                 "kidney disease":[kidneydisease], "fever":[fever], "shortness of breath":[breath], \
                "cough":[cough], "tachypnea":[tachypnea], "fatigue":[fatigue], "diarrhea":[diarrhea]}
    input_df = pd.DataFrame(input)
    filename = "LogisticRegression/predictorRisk1.sav"
    risk_model = pickle.load(open(filename, 'rb'))
    predicted_result = risk_model.predict(input_df)[0]
    print(("Predicted result : {}").format(predicted_result))
    result = {"outcome":[predicted_result]}
    result_df = pd.DataFrame(result)
    return  predicted_result


# create route that renders index.html template
@app.route("/",methods = ["GET","POST"])
def echo():
    #return render_template("index.html", text="Serving up cool text from the Flask server!!")
    
    return render_template("risk_cal.html")

@app.route("/results", methods=['GET', 'POST'])
def results():
    
      if flask.request.method == 'POST':
            age = request.form.get("age")


            if request.form.get("fever"):
               fever = 1
            else:
                fever=0
            if request.form.get("hypertension"):
                hypertension = 1
            else:
                hypertension =0
            if request.form.get("diabetes"):
                diabetes = 1
            else:
                diabetes = 0
            if request.form.get("cvd"):
                cvd = 1
            else:
                cvd = 0
            if request.form.get("copd"):
                copd = 1
            else:
                copd = 0
            if request.form.get("cancer"):
                cancer = 1
            else:
                cancer = 0
            if request.form.get("kidneydisease"):
                kidneydisease = 1
            else:
                kidneydisease = 0
            if request.form.get("fever"):
                fever = 1
            else:
                fever = 0
            if request.form.get("breath"):
                breath = 1
            else:
                breath = 0
            if request.form.get("cough"):
                cough = 1
            else:
                cough = 0
            if request.form.get("tachypnea"):
                tachypnea = 1
            else:
                tachypnea = 0
            if request.form.get("fatigue"):
                fatigue = 1
            else:
                fatigue = 0
            if request.form.get("diarrhea"):
                diarrhea = 1
            else:
                diarrhea = 0
            
            
            predicted_result = predictRisk(age, hypertension, diabetes, cvd, copd, cancer, kidneydisease, fever, breath, cough, tachypnea, fatigue, diarrhea)

            if predicted_result == 0:
                result = "Low Risk"
            else:
                result = "High Risk"
                
            return  render_template('result.html', prediction=result)

#return  f' Predicated_result :{predicted_result} Input Values are: {age} {hypertension} { diabetes } {cvd} { copd} {cancer} {kidneydisease} {fever} {breath} {cough} {tachypnea} {fatigue} {diarrhea}'



if __name__ == "__main__":
    app.run(debug=True)