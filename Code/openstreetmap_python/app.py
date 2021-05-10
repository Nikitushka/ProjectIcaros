#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy as sqlA
import json
from parsers import csv_parse, wifi_parse
import os

# initialize the app and DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/icaros'
db = sqlA(app)
db.create_all()

# map for index
@app.route("/")
def map():
    return render_template('index.html')

# neatly return all data in a json object
@app.route("/api")
def api():
    radioresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NULL").fetchall()
    wifiresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NOT NULL").fetchall()

    return {"total": (len(radioresults) + len(wifiresults)), "sdr": [dict(row) for row in radioresults], "wifi": [dict(row) for row in wifiresults]}
    
# return wifi data only or post wifi data
@app.route("/api/wifi", methods = ['GET', 'POST']) # allowed HTTP methods
def wifi():
    if request.method == 'POST':
        
        data = request.get_json()
        # call nmcli on system and write a quick scan to the specified file location (make this definable by an .env file at some point?)
        os.system("nmcli -t -m multiline dev wifi list ifname wlan1 > output/wifi_out")
        result = wifi_parse(data["lat"], data["lon"]) # parse the output file with the coords, returning a list of objects

        # prepare an insert statement and insert the parsed output an object at a time
        statement = """INSERT INTO scan(lat, lon, ssid, encryption) VALUES(%(lat)s, %(lon)s, %(SSID)s, %(SECURITY)s)"""
        for line in result:
            db.engine.execute(statement, line)
        return json.dumps(result)
        
    else:
        
        # if the HTTP method is GET, return only the wifi data
        wifiresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NOT NULL").fetchall()
        return {"total": len(wifiresults), "wifi": [dict(row) for row in wifiresults]}

# return sdr data only or post sdr data, the gist of it is the same as in the /wifi endpoint
@app.route("/api/sdr", methods = ['GET', 'POST'])
def radio():
    if request.method == 'POST':
        
        data = request.get_json()
        # call rtl_power on the system for 1 second and write the output to the specified file location
        os.system("rtl_power -1 -f 87M:107M:200k output/sdr.csv") 
        result = csv_parse(data["lat"], data["lon"])
        
        statement = """INSERT INTO scan(lat, lon, sdr_frequency, signal_strength) VALUES(%(lat)s, %(lon)s, %(sdr_frequency)s, %(signal_strength)s)"""
        for line in result:
            db.engine.execute(statement, line)
        return json.dumps(result)
        
    else:
        
        radioresults = db.engine.execute("SELECT * FROM scan WHERE ssid IS NULL").fetchall()
        return {"total": len(radioresults), "sdr": [dict(row) for row in radioresults]}

if __name__ == "__main__":
    app.run(debug=True)
