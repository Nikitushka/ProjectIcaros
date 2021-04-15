#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy as sqlA
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/icaros'
db = sqlA(app)
db.create_all()

# map
@app.route("/")
def map():
    return render_template('index.html')

# return EVERYTHING
@app.route("/api")
def api():
 
    # trying out a pure sql solution

    radioresults = db.engine.execute("SELECT * FROM sdr").fetchall()
    wifiresults = db.engine.execute("SELECT * FROM wifi").fetchall()

    return {"total": (len(radioresults) + len(wifiresults)), "sdr": [dict(row) for row in radioresults], "wifi": [dict(row) for row in wifiresults]}
    
# return wifi data only or post wifi data
@app.route("/api/wifi", methods = ['GET', 'POST'])
def wifi():
    if request.method == 'POST':
        
        data = request.get_json()
        return data["number"]
        
    else:
        
        wifiresults = db.engine.execute("SELECT * FROM wifi").fetchall()
        return {"total": len(wifiresults), "wifi": [dict(row) for row in wifiresults]}

# return sdr data only or post sdr data
@app.route("/api/sdr", methods = ['GET', 'POST'])
def radio():
    if request.method == 'POST':
        
        data = request.get_json()

    else:
        
        radioresults = db.engine.execute("SELECT * FROM sdr").fetchall()
        return {"total": len(radioresults), "sdr": [dict(row) for row in radioresults]}

def insert_wifi(frequency, lat, lon, modulation, strength):
    print("placeholder")

if __name__ == "__main__":
    app.run(debug=True)
