from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from wtforms import SelectField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'brychu'
import sqlite3



# Retrieve data from database
def getData():
    conn=sqlite3.connect('../RASPBERRYdane/dane1.db')
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM BMP1 where (pomiar='temp') ORDER BY timestamp DESC LIMIT 1"):
        time = str(row[0])
        temp = row[2]

    for row in curs.execute("SELECT * FROM BMP1 where (pomiar='pres') ORDER BY timestamp DESC LIMIT 1"):
        press = row[2]

    for row in curs.execute("SELECT * FROM BMP2 where (pomiar='temp') ORDER BY timestamp DESC LIMIT 1"):
        time2 = str(row[0])
        temp2 = row[2]

    for row in curs.execute("SELECT * FROM BMP2 where (pomiar='pres') ORDER BY timestamp DESC LIMIT 1"):
        press2 = row[2]
    return  time, temp, press, time2, temp2, press2
    conn.close()

@app.route('/')
def index():
            time, temp, press, time2, temp2, press2 = getData()
            templateData = {
            'time': time,
            'temp': temp,
            'press': press,
            'time2': time2,
            'temp2': temp2,
            'press2': press2
            }
            return render_template('index2.html', **templateData)

            
            
# main route



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5002, debug=False)
