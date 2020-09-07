from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.global_product.controller.features import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1
from functools import wraps
import jwt

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

blu_product = NestedBlueprint(blu_v1, '/globalproduct')

#-------------------To fetch Category features--------------

@blu_product.route('/categoryfeatures/<cat_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_features_global(current_user, cat_id):
    # json_data = request.json
    status = fetch_category_features_global(cat_id)
    if status == "user_check_fail":
        return make_response('User Check fail', 403)

    if status == "category_feature_not_found":
        return make_response('category Fearture not found', 204)

    return make_response(json.dumps(status), 200)

@blu_product.route('/categoryfeatureswithgroups/<cat_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_features_with_groups_global(current_user, cat_id):
    # json_data = request.json
    status = fetch_category_with_groups_features_global(cat_id)
    if status == "user_check_fail":
        return make_response('User Check fail', 403)

    if status == "category_feature_not_found":
        return make_response('category Fearture not found', 204)

    return make_response(json.dumps(status), 200)

@blu_product.route('/featuresgroups/<cat_id>', methods=["GET"])
@cross_origin()
@token_required
def fetch_feature_groups_route_global(current_user, cat_id):
    status = fetch_features_groups_global(cat_id)

    return make_response(json.dumps(status), 200)