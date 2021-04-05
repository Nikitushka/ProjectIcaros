#!/usr/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy as sqlA

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://postgres:test@localhost/icaros'
db = sqlA(app)
db.create_all()

# map
@app.route("/")
def map():
    return render_template('index.html')

# return EVERYTHING
@app.route("/api")
def api():
    # models will go here
    # radio = RadioModel.query.all()
    # wifi = WiFiModel.query.all()

    # trying out a pure sql solution

    # radioresults = db.engine.execute("SELECT * FROM sdr")
    wifiresults = db.engine.execute("SELECT * FROM wifi")

    return {"total": (len(radioresults) + len(wifiresults)), "radio": radioresults, "wifi": wifiresults}
    
    return "Hey i'm worken 'ere!"

# return wifi data only
@app.route("/api/wifi")
def wifi():
    # wifi = WifiModel.query.all()
    # wifiresults = [
        # {
        #
        #
        #
        # } for w in wifi]
    # return {"total": len(wifi), "wifi": wifiresults}

    return "Hey i'm worken 'ere!"

# return radio data only
@app.route("/api/radio")
def radio():
    # radio = RadioModel.query.all()
    # radioresults = [
        # {
        #
        #
        #
        # } for r in radio]

    # return {"total": len(radio), "radio": radioresults}
    
    return "Hey i'm worken 'ere!"

if __name__ == "__main__":
    app.run(debug=True)
