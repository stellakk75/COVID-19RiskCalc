# Import Libraries
import os
import numpy as np
import pandas as pd
import sqlalchemy
from flask_cors import CORS
from flask import Flask, render_template, redirect, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import psycopg2
import config as creds


# create instance of Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

#Define database connection
conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
                  + " password=" + creds.PGPASSWORD

print(conn_string)
conn = psycopg2.connect(conn_string)
print("Connected!")
  

covid_df = pd.read_sql_query(
                   ''' SELECT * FROM coviddata 
                   ''' , conn)

# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", text="Serving up cool text from the Flask server!!")


if __name__ == "__main__":
    app.run(debug=True)