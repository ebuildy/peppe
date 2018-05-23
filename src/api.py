from flask import Flask
from flask import jsonify
from flask import request

from flask_restplus import Api, Resource, fields

import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/api/commands"))

import cat_models
import model_api
import analyze_api

app = Flask(__name__)
api = Api(app, version='0.0.1', title='peppe',
    description='a simple fasttext HTTP wrapper',
)

@api.route("/_cat/models")
class CatModel(Resource):
    def get(self):
        return model_api.cat_models()

@api.route("/<model>/_predict")
@api.param('model', 'the model identifier')
@api.response(404, 'model not found')
@api.param('text', 'the text to analyze')
class ModelPredict(Resource):
    def get(self, model):
        text = request.args.get('text')
        return model_api.predict(model, text)

@api.route("/<model>/_words")
@api.param('model', 'the model identifier')
@api.response(404, 'model not found')
class ModelWords(Resource):
    def get(self, model):
        return model_api.words(model)

@api.route("/<model>/_labels")
@api.param('model', 'the model identifier')
@api.response(404, 'model not found')
class ModelLabels(Resource):
    def get(self, model):
        return model_api.labels(model)

@api.route("/<model>")
@api.param('model', 'the model identifier')
@api.response(404, 'model not found')
class ModelDetails(Resource):
    def get(self, model):
        return model_api.call(model)


@api.route("/_analyze")
@api.param('text', 'the text to analyze')
@api.response(200, 'success')
class AnalyzeAPI(Resource):
    def get(self):
        text = request.args.get('text')
        return analyze_api.analyze(text)

@api.errorhandler(Exception)
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

    return response, status_code

if __name__ == '__main__':
    app.run(debug=True)
