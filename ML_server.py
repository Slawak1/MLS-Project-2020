from flask import Flask, request, jsonify
import requests
import joblib


app = Flask(__name__, static_url_path="",static_folder="static")

# main page
@app.route("/")
def index():
    print("hi")
    
    return app.send_static_file("index.html")

    
# Polynomial regression
@app.route("/poly", methods=["POST"])
def poly():

    wind = {
        "wind":request.json["wind"]}
    
    loaded_model = joblib.load(r"model/polynomial_model.pkl")

    wind = float(wind["wind"])

    if wind < 3.5 or wind > 24:
        power = 0
    else:
        power = loaded_model.predict([[wind,wind**2, wind**3]])
        power = power[0][0]

    if power < 0:
        power = 0

    return {"power":power,"score":loaded_model.score()}

# Simple Linear Regression
@app.route("/linear", methods=["POST"])
def linear():

    wind = {
        "wind":request.json["wind"]}
    
    
    wind = float(wind["wind"])
    
    loaded_model = joblib.load(r"model/simple_linear_model.pkl")

    if wind < 3.5 or wind > 24:
        power = 0
    else: 
        power = loaded_model.predict([[wind]])
        power = power[0][0]

    if power < 0:
        power = 0
    
    return {"power":power}

if __name__ == '__main__':
   app.run(debug = True)