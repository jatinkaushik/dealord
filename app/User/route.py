from flask import render_template, flash, request, url_for, redirect, session, jsonify
from app.User.controller import login, register
import json
from app import app


@app.route('/signup', methods=["POST"])
def Registration_page():
    json_data = request.json
    register_status = register(json_data)
    return json.dumps(register_status)



@app.route('/login', methods=["POST"])
def login_page():
    json_data = request.json
    login_token = login(json_data)
    return json.dumps(login_token)
