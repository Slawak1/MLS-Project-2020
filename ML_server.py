from flask import Flask, request, jsonify
import requests


app = Flask(__name__, static_url_path="",static_folder="static")


@app.route("/")
def index():
    print("hi")
    
    return app.send_static_file("index.html")



    

@app.route("/poly", methods=["POST"])
def poly(data):
    print("WTF??")
    print(data)
    # float(wind) = data["wind"]
    # power = 17.02 +(-10.5719*wind)+(1.5611*(wind**2))+(-0.0410*(wind**3))    

    return data

@app.route('/login', methods = ["POST"])
def login():

    wind = {
        "wind":request.json["wind"]}
    print(wind)

    return 1

if __name__ == '__main__':
   app.run(debug = True)