from flask import render_template, flash, request, url_for, redirect, session, jsonify, make_response
import json
from app import app
from app.v1.vendors.controller import *
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

blu_vendors = NestedBlueprint(blu_v1, '/vendors')

# ------------------ create New category ------------------

@blu_vendors.route('/vendor', methods=["POST"])
@cross_origin()
@token_required
def create_vendor_route(current_user):
    json_data = request.json
    create_status = create_vendor(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_vendors.route('/vendor/<vendor_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_vendor_route(current_user,vendor_id):
    json_data = request.json
    create_status = fetch_vendor(vendor_id)
    
    return make_response(json.dumps(create_status), 200)

@blu_vendors.route('/vendorinfo', methods=["POST"])
@cross_origin()
@token_required
def vendor_info_route(current_user):
    json_data = request.json
    create_status = vendor_info(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_vendors.route('/vendorinfo/<vendor_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_vendor_info_route(current_user,vendor_id):
    json_data = request.json
    create_status = fetch_vendor_info(vendor_id)
    
    return make_response(json.dumps(create_status), 200)

@blu_vendors.route('/vendoraddress', methods=["POST"])
@cross_origin()
@token_required
def vendor_address_route(current_user):
    json_data = request.json
    create_status = vendor_address(json_data)
    
    return make_response(json.dumps(create_status), 200)

@blu_vendors.route('/vendoraddress/<vendor_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_vendor_address_route(current_user,vendor_id):
    json_data = request.json
    create_status = fetch_vendor_address(vendor_id)
    
    return make_response(json.dumps(create_status), 200)