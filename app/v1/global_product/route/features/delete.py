from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.global_product.controller.features.delete import *
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

@blu_product.route('/featuresgroups', methods=["DELETE"])
@cross_origin()
@token_required
def delete_feature_groups_route_global(current_user):
    json_data = request.json
    status = delete_features_groups_global(json_data)

    return json.dumps(status)

#---------------------Delete category Features--------------   

@blu_product.route('/categoryfeatures', methods=["DELETE"])
@cross_origin()
@token_required
def delete_category_features_route_global(current_user):
    json_data = request.json
    status = delete_category_features_global(current_user, json_data)

    if status == "category_feature_not_found":
        return make_response('category Fearture not found', 204)
    return status

@blu_product.route('/categoryfeatures/<feature_id>', methods=["DELETE"])
@cross_origin()
@token_required
def delete_features_route(current_user,feature_id):
    status = delete_features(feature_id)

    return status

@blu_product.route('/recommendation_value', methods=["DELETE"])
@cross_origin()
@token_required
def delete_recommended_particular_value_route(current_user):
    json_data = request.json
    type_id = json_data['type_id']
    status = delete_recommended_particular_value(json_data,type_id)

    return json.dumps(status)
