import numpy as np
from flask import Blueprint, request, current_app, jsonify

ROUTES = Blueprint('routes', __name__)

@ROUTES.route('/', methods=['POST'])
def index():
    formatted_features = np.array([request.get_json()['data']])
    response = current_app.iris_model.predict_proba(formatted_features)
    return jsonify(payload=response.tolist()[0])
