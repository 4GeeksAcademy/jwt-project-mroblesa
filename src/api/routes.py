"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])
def handle_login():
    
    response_body = {} 

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email, password=password).first()

    if user:
        access_token = create_access_token(identity={'user_id' : user.id , 'email': user.email })
        response_body['message'] = 'Usuario logeado'
        response_body['access_token'] = access_token
        response_body['results'] = user.serialize()
        return jsonify(response_body), 200
    else:
        response_body['message'] = 'Credenciales incorrectas'
        return jsonify(response_body), 401
    
