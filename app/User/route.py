from flask import render_template, flash, request, url_for, redirect, session, jsonify
from app.User.controller import login, register
import json
from app import app
from flask_cors import CORS, cross_origin


@app.route('/signup', methods=["POST"])
@cross_origin()
def Registration_page():
    json_data = request.json
    register_status = register(json_data)
    return json.dumps(register_status)



@app.route('/login', methods=["POST"])
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
