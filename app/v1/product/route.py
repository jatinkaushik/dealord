from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response
from app.v1.product.controller import *
import json
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1
from functools import wraps
import jwt
# from app.v1.user import User

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
            from app.v1.user import User as JK
            current_user = JK.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

blu_product = NestedBlueprint(blu_v1, '/product')



# =========================== Category =========================

# ------------------ create New category ------------------

@blu_product.route('/category', methods=["POST"])
@cross_origin()
@token_required
def create_category_route(current_user):
    json_data = request.json
    create_status = create_category(current_user, json_data)
    
    return json.dumps(create_status)

#------------------------Fetch category----------------------

@blu_product.route('/category', methods=["GET"])
@cross_origin()
@token_required
def fetch_category_route(current_user):
    status = fetch_category(current_user)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "category_not_found":
        return make_response('Category not found', 204)
    
    return json.dumps(status)

#------------------------ Delete category----------------------
@blu_product.route('/category', methods=["DELETE"])
@cross_origin()
@token_required
def delete_category_route(current_user):
    json_data = request.json
    status = delete_category(current_user,json_data)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "category_not_found":
        return make_response('Category not found', 204)

    return json.dumps(status)

#--------------------- Edit Category Name ---------------------

@blu_product.route('/category', methods = ["PUT"])
@cross_origin()
@token_required
def edit_category_route(current_user):
    json_data = request.json
    status = edit_category(current_user, json_data)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "category_not_found":
        return make_response('Category not found', 204)

    return json.dumps(status)


#===============================Sub category=======================

#----------------------create New Sub category-----------------

# @blu_product.route('/subcategory', methods=["POST"])
# @cross_origin()
# @token_required
# def create_sub_category_route(current_user):
#     json_data = request.json
#     create_status = create_sub_category(json_data)
    
#     return json.dumps(create_status)


# #---------------------Fetch Sub category-----------------------

# @blu_product.route('/subcategory', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_sub_category_route(current_user):
#     json_data = request.json
#     status = fetch_sub_category(current_user,json_data)
#     if status == "user_check_fail":
#         return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

#     if status == "subcategory_not_found":
#         return make_response('Subcategory not found', 204)
    
#     return json.dumps(status)

# #------------------------Delete subcategory--------------------   

# @blu_product.route('/subcategory', methods=["DELETE"])
# @cross_origin()
# @token_required
# def delete_subcategory_route(current_user):
#     json_data = request.json
#     status = delete_sub_category(current_user,json_data)
#     if status == "user_check_fail":
#         return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

#     if status == "subcategory_not_found":
#         return make_response('Subcategory not found', 204)
    
#     return json.dumps(status)

# #--------------------- Edit SubCategory Name ------------------

# @blu_product.route('/subcategory', methods = ["PUT"])
# @cross_origin()
# @token_required
# def edit_subcategory_route(current_user):
#     json_data = request.json
#     status = edit_subcategory(current_user, json_data)
#     if status == "user_check_fail":
#        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
#     if status == "subcategory_not_found":
#         return make_response('Subcategory not found', 204)

#     return json.dumps(status)



#=====================Category features===================

#----------------- To Add features for Category------------

@blu_product.route('/categoryfeatures', methods=["POST"])  
@cross_origin()
@token_required
def add_features():
    json_data = request.json
    status = feature_func(json_data)

    return json.dumps(status)  

#-------------------To fetch Category features--------------

@blu_product.route('/categoryfeatures', methods=["GET"])
@cross_origin()
@token_required
def fetch_features(current_user):
    json_data = request.json
    status = fetch_category_features(current_user,json_data)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "category_feature_not_found":
        return make_response('category Fearture not found', 204)

    return status

#---------------------Delete category Features--------------   

@blu_product.route('/categoryfeatures', methods=["DELETE"])
@cross_origin()
@token_required
def delete_category_features_route(current_user, json_data):
    json_data = request.json
    status = delete_category_features(current_user, json_data)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "category_feature_not_found":
        return make_response('category Fearture not found', 204)
    return status

#-------------------Edit category Features------------------

@blu_product.route('/categoryfeatures', methods = ["PUT"])
@cross_origin()
@token_required
def edit_category_featuresroute(current_user):
    json_data = request.json
    status = edit_category_features(current_user, json_data)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "category_feature_not_found":
        return make_response('category Fearture not found', 204)
    return json.dumps(status)

#-------------- To make Type of Datatype Features--------------

@blu_product.route('/featuredatatype', methods=["POST"])
@cross_origin()
@token_required
def feature_datatyperoute():
    json_data = request.json
    status = feature_datatypefunc(json_data)

    return json.dumps(status)

#======================= Product =================================

#-------------------- Add Product -----------------------------

@blu_product.route('/productdata',methods=["POST"])
@cross_origin()
@token_required
def addproductdataroute():
    json_data =request.json
    status = add_product_data(json_data)

    return status

#------------------ Product fetch -----------------------------
@blu_product.route('/productdata',methods=["GET"])
@cross_origin()
@token_required
def fetch_product():
    json_data =request.json
    status = add_product_data(json_data)
    if status == "user_check_fail":
        return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if status == "product_not_found":
        return make_response('Product not found', 204)

    return status

#------------------- TO add extra Fearture --------------------

@blu_product.route('/addextrafeature', methods=["POST"])
@cross_origin()
@token_required
def addextrafeature_route():
    json_data = request.json
    status = extra_features(json_data)

    return status

#--------------------- To add Varient -------------------------

@blu_product.route('/addvarient', methods=["POST"])
@cross_origin()
@token_required
def addvarientroute():
    json_data = request.json
    status = add_varient(json_data)

    return json.dumps(status)

