from flask import render_template, flash, request, url_for, redirect, session, jsonify, make_response
import json
from app import app
from app.v1.customers.controller import *
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

blu_customers = NestedBlueprint(blu_v1, '/customers')

# ------------------ create New category ------------------

@blu_customers.route('/customer', methods=["POST"])
@cross_origin()
@token_required
def create_customer_route(current_user):
    json_data = request.json
    create_status = create_customer(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_customers.route('/customer', methods=["PUT"])
@cross_origin()
@token_required
def edit_customer_route(current_user):
    json_data = request.json
    create_status = edit_customer(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_customers.route('/customer/<customer_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_customer_route(current_user,customer_id):
    create_status = fetch_customer(customer_id)
    
    return make_response(json.dumps(create_status), 200)

@blu_customers.route('/customerinfo', methods=["POST"])
@cross_origin()
@token_required
def customer_info_route(current_user):
    json_data = request.json
    create_status = customer_info(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_customers.route('/customerinfo/<customer_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_customer_info_route(current_user,customer_id):
    create_status = fetch_customer_info(customer_id)
    
    return make_response(json.dumps(create_status), 200)

@blu_customers.route('/customeraddress', methods=["POST"])
@cross_origin()
@token_required
def customer_address_route(current_user):
    json_data = request.json
    create_status = customer_address(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_customers.route('/customeraddress/<customer_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_customer_address_route(current_user,customer_id):
    create_status = fetch_customer_address(customer_id)
    
    return make_response(json.dumps(create_status), 200)

