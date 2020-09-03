from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.global_product.controller.product.add import *
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

#-------------------- Add Product -----------------------------

@blu_product.route('/product',methods=["POST"])
@cross_origin()
@token_required
def add_product_data_global_route(current_user):
    json_data =request.json
    status = add_product_global(json_data)

    return json.dumps(status)
            
@blu_product.route('/initializing_product',methods=["POST"])
@cross_origin()
@token_required
def add_product_with_image_route(current_user):
    images = request.files
    json_data = request.form
    status = add_product_with_image(images,json_data)

    return json.dumps(status)
    
#------------------ Product Features Data----------------------

@blu_product.route('/productvarient',methods=["POST"])
@cross_origin()
@token_required
def product_features_route(current_user):
    json_data = request.json
    product_varient_id = json_data['product_varient_id']
    status = product_features(json_data,product_varient_id)

    return status