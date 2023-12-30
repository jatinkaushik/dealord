from flask import render_template, flash, request, url_for, redirect, session, jsonify, make_response
import json
from app import app
from app.v1.items.controller import *
import datetime
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1
from app import db
import jwt
from functools import wraps

#========================= Token Verification ==========================

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            from app.v1.user import UserUser as JK
            current_user = JK.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

blu_items = NestedBlueprint(blu_v1, '/items')


@blu_items.route('/items', methods=["POST"])
@cross_origin()
@token_required
def add_product_route(current_user):
    json_data = request.json
    create_status = add_product(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_items.route('/items', methods=["GET"])
@cross_origin()
@token_required
def fetch_product_route(current_user):
    json_data = request.json
    create_status = fetch_product(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_items.route('/items', methods=["PUT"])
@cross_origin()
@token_required
def edit_product_route(current_user):
    json_data = request.json
    create_status = edit_product(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_items.route('/items', methods=["DELETE"])
@cross_origin()
@token_required
def delete_product_route(current_user):
    json_data = request.json
    create_status = delete_product(json_data)
    
    return make_response(json.dumps(create_status), 200)


