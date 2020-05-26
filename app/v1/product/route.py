from flask import render_template, flash, request, url_for, redirect, session, jsonify
from app.v1.product.controller import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1

blu_product = NestedBlueprint(blu_v1, '/product')

#create New category
@blu_product.route('/newcategory', methods=["POST"])
@cross_origin()
def create_category_route():
    json_data = request.json
    create_status = create_category(json_data)
    
    return json.dumps(create_status)

#create New Sub category
@blu_product.route('/newsubcategory', methods=["POST"])
@cross_origin()
def create_sub_category_route():
    json_data = request.json
    create_status = create_sub_category(json_data)
    
    return json.dumps(create_status)

#Fatch category
@blu_product.route('/category', methods=["POST"])
@cross_origin()
def fetch_category_route():
    json_data = request.json
    status = fetch_category(json_data)
    
    return json.dumps(status)

#create New Sub category
@blu_product.route('/subcategory', methods=["POST"])
@cross_origin()
def fetch_sub_category_route():
    json_data = request.json
    status = fetch_sub_category(json_data)
    
    return json.dumps(status)

# To Add features for Sub Category
@blu_product.route('/addsubcategoryfeatures', methods=["POST"])  
@cross_origin()
def add_features():
    json_data = request.json
    status = feature_func(json_data)

    return json.dumps(status)  

#To fetch SubCategory
@blu_product.route('/fetchsubcategoryfeatures', methods=["POST"])
@cross_origin()
def fetch_features():
    json_data = request.json
    status = get_sub_category_features(json_data)

    return status

#To make Type of Datatype
@blu_product.route('/featuredatatype', methods=["POST"])
@cross_origin()
def feature_datatyperoute():
    json_data = request.json
    status = feature_datatypefunc(json_data)

    return json.dumps(status)


@blu_product.route('/addproductdata',methods=["POST"])
@cross_origin()
def addproductdataroute():
    json_data =request.json
    status = add_product_data(json_data)

    return status

@blu_product.route('/addextrafeature', methods=["POST"])
@cross_origin()
def addextrafeature_route():
    json_data = request.json
    status = extra_features(json_data)

    return status

@blu_product.route('/addvarient', methods=["POST"])
@cross_origin()
def addvarientroute():
    json_data = request.json
    status = add_varient(json_data)

    return json.dumps(status)

