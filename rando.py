import flask as fl
import numpy as np


app = fl.Flask(__name__)

@app.route("/")

def home():
    return "Helo World"

@app.route("/uniform")
def uniform():
    return {"value":np.random.uniform()}

@app.route("/normal")
def normal():
    return {"value":np.random.normal()}