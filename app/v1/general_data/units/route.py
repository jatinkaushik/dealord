from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.general_data.units.controller import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1

blu_product = NestedBlueprint(blu_v1, '/generaldata/units')

#========================= Token Verification ==========================

from functools import wraps
import jwt

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


@blu_product.route('/typesunits', methods=["POST"])
@cross_origin()
@token_required
def feature_units_types_route(current_user):
    json_data = request.json
    status = feature_units_types_global(json_data)

    return json.dumps(status)

@blu_product.route('/units', methods=["GET"])
@cross_origin()
@token_required
def fetch_feature_units_route(current_user):
    # json_data = request.json
    status = fetch_feature_units_global()

    return json.dumps(status)

#-----------------------To Add Units---------------------------
@blu_product.route('/units', methods=["POST"])
@cross_origin()
@token_required
def add_units_route(current_user):
    json_data = request.json
    status = add_units(json_data)

    return status

@blu_product.route('/units/<units_type_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_units_route(current_user,units_type_id):
    # json_data = request.json
    status = fetch_add_units(units_type_id)
    return json.dumps(status)