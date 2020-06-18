from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response
from app.v1.employee.basic_detail import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1

blu_product = NestedBlueprint(blu_v1, '/employee')

@blu_product.route('/employeebasic', methods=["POST"])
@cross_origin()
def employee_basic_route():
    json_data = request.json
    create_status = employee_basic(json_data)
    
    return (create_status)


@blu_product.route('/employeebasic', methods=["GET"])
@cross_origin()
def fetch_employee_basic_route():
    json_data = request.json
    create_status = fetch_employee_basic(json_data)
    
    return json.dumps(create_status)

@blu_product.route('/employeebasic', methods=["PUT"])
@cross_origin()
def edit_employee_basic_route():
    json_data = request.json
    create_status = edit_employee_basic(json_data)
    
    return json.dumps(create_status)

@blu_product.route('/employeebasic', methods=["DELETE"])
@cross_origin()
def delete_employee_basic_route():
    json_data = request.json
    create_status = delete_employee_basic(json_data)
    
    return json.dumps(create_status)

@blu_product.route('/personaldetail', methods=["POST"])
@cross_origin()
def addpersonal_detail_route():
    json_data = request.json
    create_status = addpersonal_detail(json_data)
    
    return json.dumps(create_status)

@blu_product.route('/personaldetail', methods=["GET"])
@cross_origin()
def fetch_personal_detail_route():
    json_data = request.json
    create_status = fetch_personal_detail(json_data)
    
    return json.dumps(create_status)

@blu_product.route('/personaldetail', methods=["PUT"])
@cross_origin()
def edit_personal_detail_route():
    json_data = request.json
    create_status = edit_personal_detail(json_data)
    
    return json.dumps(create_status)

@blu_product.route('/personaldetail', methods=["DELETE"])
@cross_origin()
def delete_employee_personal_detail_route():
    json_data = request.json
    create_status = delete_employee_personal_detail(json_data)
    
    return json.dumps(create_status)

