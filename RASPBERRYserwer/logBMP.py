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

# dane statystyczne
def getStats():
    conn=sqlite3.connect('../RASPBERRYdane/dane.db')
    curs=conn.cursor()

    for row in curs.execute("SELECT max(wartosc) FROM BMP1 where (pomiar='temp')"):
        tempMax = row[0]
        
    for row in curs.execute("SELECT max(wartosc) FROM BMP2 where (pomiar='temp')"):
        tempMax2 = row[0]
        
    for row in curs.execute("SELECT min(wartosc) FROM BMP1 where (pomiar='temp')"):
        tempMin = row[0]
        
    for row in curs.execute("SELECT min(wartosc) FROM BMP2 where (pomiar='temp')"):
        tempMin2 = row[0]
        
    for row in curs.execute("SELECT max(wartosc) FROM BMP1 where (pomiar='pres')"):
        presMax = row[0]
        
    for row in curs.execute("SELECT max(wartosc) FROM BMP2 where (pomiar='pres')"):
        presMax2 = row[0]
    
    for row in curs.execute("SELECT min(wartosc) FROM BMP1 where (pomiar='pres')"):
        presMin = row[0]
        
    for row in curs.execute("SELECT min(wartosc) FROM BMP2 where (pomiar='pres')"):
        presMin2 = row[0]
        
    for row in curs.execute("SELECT avg(wartosc) FROM BMP1 where (pomiar='pres')"):
        avgPres = row[0]
        avgPres=round(avgPres,2)
        
    for row in curs.execute("SELECT avg(wartosc) FROM BMP2 where (pomiar='pres')"):
        avgPres2 = row[0]
        avgPres2=round(avgPres2,2)
        
    for row in curs.execute("SELECT avg(wartosc) FROM BMP1 where (pomiar='temp')"):
        avgTemp = row[0]
        avgTemp=round(avgTemp,2)
        
    for row in curs.execute("SELECT avg(wartosc) FROM BMP2 where (pomiar='temp')"):
        avgTemp2 = row[0]
        avgTemp2=round(avgTemp2,2)
    
    return  tempMax, tempMax2, tempMin, tempMin2, presMax, presMax2, presMin, presMin2, avgPres, avgPres2, avgTemp, avgTemp2
    conn.close()

@app.route("/data.json")
def data():
    connection = sqlite3.connect("../RASPBERRYdane/dane.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP1 where (pomiar='temp')")
    results = cursor.fetchall()
    #print (results)
    return json.dumps(results)

@app.route("/data1.json")
def data1():
    connection = sqlite3.connect("../RASPBERRYdane/dane.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP2 where (pomiar='temp')")
    results = cursor.fetchall()
    #print (results)
    return json.dumps(results)

@app.route("/data2.json")
def data2():
    connection = sqlite3.connect("../RASPBERRYdane/dane.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP1 where (pomiar='pres')")
    results = cursor.fetchall()
    #print (results)
    return json.dumps(results)

@app.route("/data3.json")
def data3():
    connection = sqlite3.connect("../RASPBERRYdane/dane.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Cast ((JulianDay(timestamp) - JulianDay('1970-01-01')) * 24 * 60 * 60  As Integer)*1000, wartosc from BMP2 where (pomiar='pres')")
    results = cursor.fetchall()
    #print (results)
    return json.dumps(results)

 
@app.route("/graph")
def graph():
    return render_template('graph.html')

@app.route('/')
def index():
            time1, temp, press, time2, temp2, press2 = getData()
            tempMax, tempMax2, tempMin, tempMin2, presMax, presMax2, presMin, presMin2, avgPres, avgPres2, avgTemp, avgTemp2 = getStats()
            templateData = {
            'time1': time1,
            'temp': temp,
            'press': press,
            'time2': time2,
            'temp2': temp2,
            'press2': press2,
            'tempMax': tempMax,
            'tempMax2': tempMax2,
            'tempMin': tempMin,
            'tempMin2': tempMin2,
            'presMax': presMax,
            'presMax2': presMax2,
            'presMin': presMin,
            'presMin2': presMin2,
            'avgPres': avgPres,
            'avgPres2': avgPres2,
            'avgTemp': avgTemp,
            'avgTemp2': avgTemp2
            }
            return render_template('index.html', **templateData)


# main route



if __name__ == "__main__":
#    app.run(host='192.168.0.200', port=5000, debug=False)
    app.run(host='0.0.0.0', port=5000, debug=False)
