from flask import render_template, flash, request, url_for, redirect, session, jsonify
from .controller import login, register
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1

blu_user = NestedBlueprint(blu_v1, '/user')


@blu_user.route('/signup', methods=["POST"])
@cross_origin()
def Registration_page():
    json_data = request.json
    register_status = register(json_data)
    # if register_status == "Done":
        # login_temp = {
        #     "login": json_data.username,
        #     "password": json_data.password
        # }
        # login_done = login(login_temp)
        # login_done = "Done"
        # return json.dumps(login_done)
    return json.dumps(register_status)



@blu_user.route('/login', methods=["POST"])
@cross_origin()
def login_page():
    json_data = request.json
    login_token = login(json_data)
    data = {
        'user': {
            'id': 4,
            'email': "jatinkaushik@gmail.com",
            'password': "jatin",
            'name': "Jatin Kaushik"
        },
        'accessToken' : login_token
    }
    return json.dumps(data)
