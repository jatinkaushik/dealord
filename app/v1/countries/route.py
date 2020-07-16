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
    status = fetch_country()
    
    return json.dumps(status)
    

@blu_product.route('/addcountry', methods=["GET"])
@cross_origin()
def add_country_route():
    status = add_country()
    return json.dumps(status)