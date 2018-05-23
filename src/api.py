from flask import Flask
from flask import jsonify
from flask import request

import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/api/commands"))

import cat_models
import model_api

app = Flask("peppe")

@app.route("/")
def hello():
    return jsonify({"version" : "0.0.1", "name" : "peppe"})

@app.route("/_cat/models")
def cat_models():
    return jsonify(model_api.cat_models())

@app.route("/<model>/_predict")
def query(model):
    text = request.args.get('text')
    return jsonify(model_api.predict(model, text))

@app.route("/<model>/_words")
def model_words(model):
    return jsonify(model_api.words(model))

@app.route("/<model>/_labels")
def model_labels(model):
    return jsonify(model_api.labels(model))

@app.route("/<model>")
def model(model):
    return jsonify(model_api.call(model))

@app.errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]

    status_code = 500 #error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code
