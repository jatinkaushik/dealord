from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.general_data.datatypes.controller import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1

blu_product = NestedBlueprint(blu_v1, '/generaldata/datatypes')

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

#-------------- To make Type of Datatype Features--------------

@blu_product.route('/featuredatatype', methods=["POST"])
@cross_origin()
@token_required
def feature_datatype_route(current_user):
    json_data = request.json
    status = feature_datatypefunc_global(json_data)

    return json.dumps(status)

@blu_product.route('/featuredatatype', methods=["GET"])
@cross_origin()
@token_required
def fetch_datatypefunc_route(current_user):
    json_data = request.json
    status = fetch_datatypefunc_global(json_data)

    return json.dumps(status)


