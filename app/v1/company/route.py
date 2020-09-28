from flask import render_template, flash, request, url_for, redirect, session, jsonify, make_response
import json
from app import app
from app.v1.company.controller import *
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

blu_company = NestedBlueprint(blu_v1, '/company')

# ------------------ create New company ------------------

@blu_company.route('/company', methods=["POST"])
@cross_origin()
@token_required
def create_company_route(current_user):
    json_data = request.json
    create_status = create_company(current_user, json_data)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/company/<company_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_company_route(current_user,company_id):
    json_data = request.json
    create_status = fetch_company(company_id)
    
    return make_response(json.dumps(create_status), 201)


@blu_company.route('/companyinfo', methods=["POST"])
@cross_origin()
@token_required
def company_info_route(current_user):
    json_data = request.json
    company_id = json_data['json_data']
    create_status = company_info(json_data,company_id)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companyinfo/<company_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_company_info_route(current_user,company_id):
    json_data = request.json
    create_status = fetch_company_info(company_id)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companyaddress', methods=["POST"])
@cross_origin()
@token_required
def company_address_route(current_user):
    json_data = request.json
    company_id = json_data['json_data']
    create_status = company_address(json_data,company_id)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companyaddress/<company_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_company_address_route(current_user,company_id):
    json_data = request.json
    create_status = fetch_company_address(company_id)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companyall/<company_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_all_company_info_route(current_user,company_id):
    json_data = request.json
    create_status = fetch_all_company_info(company_id)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companypermission', methods=["POST"])
@cross_origin()
@token_required
def add_company_permission_route(current_user):
    json_data = request.json
    create_status = add_company_permission(json_data)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companypermission', methods=["PUT"])
@cross_origin()
@token_required
def edit_company_permission_route(current_user):
    json_data = request.json
    create_status = edit_company_permission(json_data)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companypermission', methods=["GET"])
@cross_origin()
@token_required
def fetch_company_permission_route(current_user):
    json_data = request.json
    create_status = fetch_company_permission()
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companyroles', methods=["POST"])
@cross_origin()
@token_required
def create_company_roles_route(current_user):
    json_data = request.json
    create_status = add_company_roles_route(json_data)
    
    return make_response(json.dumps(create_status), 201)

@blu_company.route('/companyroles', methods=["EDIT"])
@cross_origin()
@token_required
def edit_company_roles_route(current_user):
    json_data = request.json
    create_status = edit_company_roles_route(json_data)
    
    return make_response(json.dumps(create_status), 201)