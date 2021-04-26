#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy as sqlA
import json
from parsers import csv_parse, wifi_parse
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/icaros'
app.config.from_pyfile('config.py')
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

    radioresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NULL").fetchall()
    wifiresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NOT NULL").fetchall()

    return {"total": (len(radioresults) + len(wifiresults)), "sdr": [dict(row) for row in radioresults], "wifi": [dict(row) for row in wifiresults]}
    
# return wifi data only or post wifi data
@app.route("/api/wifi", methods = ['GET', 'POST'])
def wifi():
    if request.method == 'POST':
        
        data = request.get_json()
        # return data
        os.system("nmcli -t -m multiline dev wifi list ifname wlan1 > output/wifi_out")
        result = wifi_parse(data["lat"], data["lon"])

        statement = """INSERT INTO scan(lat, lon, ssid, encryption) VALUES(%(lat)s, %(lon)s, %(SSID)s, %(SECURITY)s)"""
        for line in result:
            db.engine.execute(statement, line)
        return json.dumps(result)
        
    else:
        
        wifiresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NOT NULL").fetchall()
        return {"total": len(wifiresults), "wifi": [dict(row) for row in wifiresults]}

# return sdr data only or post sdr data
@app.route("/api/sdr", methods = ['GET', 'POST'])
def radio():
    if request.method == 'POST':
        
        data = request.get_json()
        os.system("rtl_power -1 -f 87M:107M:200k output/sdr.csv")
        result = csv_parse(data["lat"], data["lon"])
        
        statement = """INSERT INTO scan(lat, lon, sdr_frequency, signal_strength) VALUES(%(lat)s, %(lon)s, %(sdr_frequency)s, %(signal_strength)s)"""
        for line in result:
            db.engine.execute(statement, line)
        return json.dumps(result)
        


    else:
        
        radioresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NULL").fetchall()
        return {"total": len(radioresults), "sdr": [dict(row) for row in radioresults]}

def insert_wifi(frequency, lat, lon, modulation, strength):
    print("placeholder")

if __name__ == "__main__":
    app.run(debug=True)
