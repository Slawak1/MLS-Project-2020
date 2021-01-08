from flask import Flask, request, jsonify
import requests
import joblib


# create Flask app
app = Flask(__name__, static_url_path="",static_folder="static")

# main page
@app.route("/")
def index():
    print("hi")
    
    return app.send_static_file("index.html")

    
# Polynomial regression
@app.route("/poly", methods=["POST"])
def poly():
    

    # get JSON data
    wind = {
        "wind":request.json["wind"]}
    
    # load trained model
    loaded_model = joblib.load(r"model/polynomial_model.pkl")

    # convert string to float type
    wind = float(wind["wind"])

    # if wind less that 3.5 m/s power output is equal 0 - less than cut-in speed 
    # if wind more than 24.5  the wind turbine is shutted down
    if wind < 3.5 or wind > 24:
        power = 0
    else:
        power = loaded_model.predict([[wind,wind**2, wind**3]])
        power = round(power[0][0],2)

    # in the case of wind turbines we should not get a negative power result. therefore it is set to 0 for each negative result
    if power < 0:
        power = 0

    return {"power":power}

# Simple Linear Regression
@app.route("/linear", methods=["POST"])
def linear():

    # get JSON data
    wind = {
        "wind":request.json["wind"]}
    
    # convert string to float type
    wind = float(wind["wind"])
    
    # load trained model 
    loaded_model = joblib.load(r"model/simple_linear_model.pkl")

    # if wind less that 3.5 m/s power output is equal 0 - less than cut-in speed 
    # if wind more than 24.5  the wind turbine is shutted down
    if wind < 3.5 or wind > 24.5:
        power = 0
    else: 
        power = loaded_model.predict([[wind]])
        power = round(power[0][0],2)

    # in the case of wind turbines we should not get a negative power result. therefore it is set to 0 for each negative result
    if power < 0:
        power = 0
    
    return {"power":power}

if __name__ == '__main__':
   app.run(debug = True)