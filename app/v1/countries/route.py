from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.countries.controller import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1

blu_product = NestedBlueprint(blu_v1, '/countries')

@blu_product.route('/country', methods=["GET"])
@cross_origin()
def fetch_country_route():
    json_data = request.json
    status = fetch_country(json_data)
    
    return json.dumps(status)