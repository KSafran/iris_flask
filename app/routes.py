from flask import Blueprint, request, current_app, jsonify

ROUTES = Blueprint('routes', __name__)

@ROUTES.route('/', methods=['POST'])
def index():
    response = current_app.iris_model.predict(request.get_json())
    return jsonify(payload='placeholder')
