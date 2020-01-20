from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from wtforms import SelectField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'brychu'
import sqlite3
import json
import time
import datetime


# Retrieve data from database
def getData():
    conn=sqlite3.connect('../RASPBERRYdane/dane.db')
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM BMP1 where (pomiar='temp') ORDER BY timestamp DESC LIMIT 1"):
        time1= str(row[0])
        
        temp = row[2]

    for row in curs.execute("SELECT * FROM BMP1 where (pomiar='pres') ORDER BY timestamp DESC LIMIT 1"):
        press = row[2]

    for row in curs.execute("SELECT * FROM BMP2 where (pomiar='temp') ORDER BY timestamp DESC LIMIT 1"):
        time2 = str(row[0])
        temp2 = row[2]

    for row in curs.execute("SELECT * FROM BMP2 where (pomiar='pres') ORDER BY timestamp DESC LIMIT 1"):
        press2 = row[2]
    return  time1, temp, press, time2, temp2, press2
    conn.close()

@app.route("/data.json")
def data():
    connection = sqlite3.connect("../RASPBERRYdane/dane.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP1 where (pomiar='temp')")
    results = cursor.fetchall()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP1 where (pomiar='pres')")
    results2 = cursor.fetchall()
    #print (results)
    return json.dumps(results,results2)

def data1():
    connection = sqlite3.connect("../RASPBERRYdane/dane.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP1 where (pomiar='pres')")
    results2 = cursor.fetchall()
    #print (results)
    return json.dumps(results2)

 
@app.route("/graph")
def graph():
    return render_template('graph.html')

@app.route('/')
def index():
            time1, temp, press, time2, temp2, press2 = getData()
            templateData = {
            'time1': time1,
            'temp': temp,
            'press': press,
            'time2': time2,
            'temp2': temp2,
            'press2': press2
            }
            return render_template('index2.html', **templateData)


# main route



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=False)
