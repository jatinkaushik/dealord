from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.global_product.controller.product.edit import *
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