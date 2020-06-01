from flask import render_template, flash, request, url_for, redirect, session, jsonify, make_response
from .controller import login, register, user_info
import json
from app import app
import datetime
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import jwt
from app.v1.product.route import token_required

blu_user = NestedBlueprint(blu_v1, '/user')


@blu_user.route('/signup', methods=["POST"])
@cross_origin()
def Registration_page():
    json_data = request.json
    register_status = register(json_data)
    return json.dumps(register_status)




@blu_user.route('/login', methods=["POST"])
@cross_origin()
def login_page():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    login_token = login(auth)
    return login_token

@blu_user.route('/user', methods=["GET"])
@cross_origin()
@token_required
def user_data(current_user):
    user = user_info(current_user)

    return json.dumps(user)

@blu_user.route('/verifyemail', methods=["GET"])
@cross_origin()
def verify_email():
    json_data = request.data
    check_email = User.query.filter_by(email=json_data['email']).first()

    if check_email:
        return json.dumps('email_exist')
    
    return json.dumps('email_available')

@blu_user.route('/verifyphone', methods=["GET"])
@cross_origin()
def verify_phone():
    json_data = request.data
    check_phone = User.query.filter_by(phone=json_data['phone']).first()

    if check_phone:
        return json.dumps('phone_exist')
    
    return json.dumps('phone_available')

@blu_user.route('/verifyusername', methods=["GET"])
@cross_origin()
def verify_username():
    json_data = request.data
    check_username = User.query.filter_by(username=json_data['username']).first()
    
    if check_username:
        return json.dumps('username_exist')
    
    return json.dumps('username_available')