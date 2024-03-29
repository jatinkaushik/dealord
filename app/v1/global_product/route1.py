from flask import render_template, flash, request, url_for, redirect, session, jsonify , make_response ,send_file
from app.v1.global_product.controller1 import *
import json
# from app.v1.global_product.model import *
from app import app
from flask_cors import CORS, cross_origin
from app.NestedBlueprint import NestedBlueprint
from app.v1 import blu_v1
from functools import wraps
import jwt
import os


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
            from app.v1.user import UserUser as JK
            current_user = JK.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

blu_product = NestedBlueprint(blu_v1, '/globalproduct')



# =========================== Category =========================

# ------------------ create New category ------------------

# @blu_product.route('/category', methods=["POST"])
# @cross_origin()
# @token_required
# def create_category_route_global(current_user):
#     json_data = request.json
#     create_status = create_category_global(current_user, json_data)
    
#     return json.dumps(create_status)

# #------------------------Fetch category----------------------

# @blu_product.route('/category', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_category_route_global(current_user):
#     status = fetch_category_global()
#     if status == "user_check_fail":
#         return make_response('User Check fail', 403)

#     if status == "category_not_found":
#         return make_response('Category not found', 204)
    
#     return json.dumps(status)

# #------------------------ Delete category----------------------
# @blu_product.route('/category', methods=["DELETE"])
# @cross_origin()
# @token_required
# def delete_category_route_global(current_user):
#     json_data = request.json
#     status = delete_category_global(current_user,json_data)
#     if status == "user_check_fail":
#         return make_response('User Check fail', 403)

#     if status == "category_not_found":
#         return make_response('Category not found', 204)

#     return json.dumps(status)

# #--------------------- Edit Category Name ---------------------

# @blu_product.route('/category', methods = ["PUT"])
# @cross_origin()
# @token_required
# def edit_category_route_global(current_user):
#     json_data = request.json
#     status = edit_category_global(current_user, json_data)
#     # if status == "user_check_fail":
#     #     return make_response('User Check fail', 403)

#     if status == "category_not_found":
#         return make_response('Category not found', 204)

#     return json.dumps(status)

# #--------------Fetch Sub category With parent id---------------

# @blu_product.route('/subcategory/<cat_id>', methods = ["GET"])
# @cross_origin()
# # @token_required
# def fetch_sub_category_route(cat_id):
#     # json_data = request.json
#     status = fetch_sub_category(cat_id)

#     return json.dumps(status)



#===============================Sub category=======================

#----------------------create New Sub category-----------------

# @blu_product.route('/subcategory', methods=["POST"])
# @cross_origin()
# @token_required
# def create_sub_category_route(current_user):
#     json_data = request.json
#     create_status = create_sub_category(json_data,current_user)
    
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

# @blu_product.route('/categoryfeatures', methods=["POST"])  
# @cross_origin()
# @token_required
# def add_features_global(current_user):
#     json_data = request.json
#     status = feature_func_global(json_data)

#     return json.dumps(status)  

#-------------------To fetch Category features--------------

# @blu_product.route('/categoryfeatures/<cat_id>', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_features_global(current_user, cat_id):
#     # json_data = request.json
#     status = fetch_category_features_global(cat_id)
#     if status == "user_check_fail":
#         return make_response('User Check fail', 403)

#     if status == "category_feature_not_found":
#         return make_response('category Fearture not found', 204)

#     return json.dumps(status)

# @blu_product.route('/categoryfeatureswithgroups/<cat_id>', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_features_with_groups_global(current_user, cat_id):
#     # json_data = request.json
#     status = fetch_category_with_groups_features_global(cat_id)
#     if status == "user_check_fail":
#         return make_response('User Check fail', 403)

#     if status == "category_feature_not_found":
#         return make_response('category Fearture not found', 204)

#     return json.dumps(status)

# #----------------Features Groups Function -------------------
# @blu_product.route('/featuresgroups', methods=["POST"])
# @cross_origin()
# @token_required
# def feature_groups_route_global(current_user):
#     json_data = request.json
#     status = features_groups_global(json_data)

#     return json.dumps(status)

# @blu_product.route('/featuresgroups/<cat_id>', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_feature_groups_route_global(current_user, cat_id):
#     status = fetch_features_groups_global(cat_id)

#     return json.dumps(status)

# @blu_product.route('/featuresgroups', methods=["DELETE"])
# @cross_origin()
# @token_required
# def delete_feature_groups_route_global(current_user):
#     json_data = request.json
#     status = delete_features_groups_global(json_data)

#     return json.dumps(status)

# #---------------------Delete category Features--------------   

# @blu_product.route('/categoryfeatures', methods=["DELETE"])
# @cross_origin()
# @token_required
# def delete_category_features_route_global(current_user):
#     json_data = request.json
#     status = delete_category_features_global(current_user, json_data)

#     if status == "category_feature_not_found":
#         return make_response('category Fearture not found', 204)
#     return status

# @blu_product.route('/categoryfeatures/<feature_id>', methods=["DELETE"])
# @cross_origin()
# @token_required
# def delete_features_route(current_user,feature_id):
#     status = delete_features(feature_id)

#     return status
#-------------------Edit category Features---------------------

# @blu_product.route('/categoryfeatures', methods = ["PUT"])
# @cross_origin()
# @token_required
# def edit_category_featuresroute_global(current_user):
#     json_data = request.json
#     status = edit_category_features_global(json_data)

#     # if status == "category_feature_not_found":
#     #     return make_response('category Fearture not found', 204)
#     return json.dumps(status)

# @blu_product.route('/categoryfeaturestest', methods = ["PUT"])
# @cross_origin()
# @token_required
# def edit_category_features_with_check_global_route(current_user):
#     json_data = request.json
#     status = edit_category_features_with_check_global(json_data)

#     # if status == "category_feature_not_found":
#     #     return make_response('category Fearture not found', 204)
#     return json.dumps(status)

# @blu_product.route('/featurestypesunits', methods=["POST"])
# @cross_origin()
# @token_required
# def feature_units_types_route_global(current_user):
#     json_data = request.json
#     status = feature_units_types_global(json_data)

#     return json.dumps(status)

# @blu_product.route('/featuresunits', methods=["POST"])
# @cross_origin()
# @token_required
# def feature_units_route_global(current_user):
#     json_data = request.json
#     status = feature_units_global(json_data)

    # return json.dumps(status)

# @blu_product.route('/featuresunits', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_feature_units_route_global(current_user):
#     # json_data = request.json
#     status = fetch_feature_units_global()

#     return json.dumps(status)

#-------------- To make Type of Datatype Features--------------

# @blu_product.route('/featuredatatype', methods=["POST"])
# @cross_origin()
# @token_required
# def feature_datatyperoute_global(current_user):
#     json_data = request.json
#     status = feature_datatypefunc_global(json_data)

#     return json.dumps(status)

# @blu_product.route('/featuredatatype', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_datatypefunc_route_global(current_user):
#     json_data = request.json
#     status = fetch_datatypefunc_global(json_data)

#     return json.dumps(status)

# @blu_product.route('/recommendation_value', methods=["DELETE"])
# @cross_origin()
# @token_required
# def delete_recommended_particular_value_route(current_user):
#     json_data = request.json
#     type_id = json_data['type_id']
#     status = delete_recommended_particular_value(json_data,type_id)

#     return json.dumps(status)


# @blu_product.route('/recommendation_value', methods=["PUT"])
# @cross_origin()
# @token_required
# def edit_recommended_particular_value_route(current_user):
#     json_data = request.json
#     type_id = json_data['type_id']
#     status = edit_recommended_particular_value(json_data,type_id)

#     return json.dumps(status)

#======================= Product =================================

#-------------------- Add Product -----------------------------

# @blu_product.route('/product',methods=["POST"])
# @cross_origin()
# @token_required
# def add_product_data_global_route(current_user):
#     json_data =request.json
#     status = add_product_global(json_data)

#     return json.dumps(status)

# @blu_product.route('/initializing_product',methods=["POST"])
# @cross_origin()
# @token_required
# def add_product_with_image_route(current_user):
#     images = request.files
#     json_data = request.form
#     status = add_product_with_image(images,json_data)

#     return json.dumps(status)

#------------------ Product fetch -----------------------------
# @blu_product.route('/product',methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_product_globalcurrent(current_user):
#     json_data =request.json
#     status = add_product_data_global(json_data)
#     if status == "user_check_fail":
#         return make_response('User Check fail', 403)

#     if status == "product_not_found":
#         return make_response('Product not found', 204)

#     return status

#------------------ Product Features Data----------------------

# @blu_product.route('/productvarient',methods=["POST"])
# @cross_origin()
# @token_required
# def product_features_route(current_user):
#     json_data = request.json
#     product_varient_id = json_data['product_varient_id']
#     status = product_features(json_data,product_varient_id)

#     return status

# @blu_product.route('/productvarient',methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_product_varient_route(current_user):
#     json_data = request.json
#     status = fetch_product_varient(json_data)

#     return json.dumps(status)

@blu_product.route('/allproductvarient',methods=["GET"])
@cross_origin()
@token_required
def fetch_all_product_varient_route(current_user):
    # json_data = request.json
    status = fetch_all_product()

    return json.dumps(status)


#------------------- TO add extra Fearture --------------------

@blu_product.route('/extrafeature', methods=["POST"])
@cross_origin()
@token_required
def addextrafeature_route_global(current_user):
    json_data = request.json
    status = extra_features_global(json_data)

    return status

#--------------------- To add Varient -------------------------

@blu_product.route('/enblevarient', methods=["POST"])
@cross_origin()
@token_required
def addvarientroute_global(current_user):
    json_data = request.json
    status = add_varient_global(json_data)

    return json.dumps(status)

#-----------------------To Add Units---------------------------
# @blu_product.route('/units', methods=["POST"])
# @cross_origin()
# @token_required
# def add_units_route(current_user):
#     json_data = request.json
#     status = add_units(json_data)

#     return status

# @blu_product.route('/units/<units_type_id>', methods=["GET"])
# @cross_origin()
# @token_required
# def fetch_units_route(current_user,units_type_id):
#     # json_data = request.json
#     status = fetch_add_units(units_type_id)
#     return json.dumps(status)

@blu_product.route('/uploadimage', methods=["POST"])
@cross_origin()
@token_required
def upload_image_route(current_user):
    images = request.files
    json_data = request.form
    status = upload_image(images,json_data)
    return json.dumps(status)


@blu_product.route('/justchill', methods=["GET"])
@cross_origin()
def testing_route():
    # os.chdir("./static/img")
    # path = os.getcwd()
    url = "http://127.0.0.1:5000"+app.config['IMAGE_UPLOADS']
    return json.dumps(url)


@blu_product.route('/static/img/<file>', methods=["GET"])
@cross_origin()
# @token_required
def fetch_test_image_route(file):
    path = '../static/img/'+ file
    image = send_file(path , attachment_filename = file)
    return image
    
# http://127.0.0.1:5000/v1/globalproduct/static/img/Pizza_Momos_Finger_Dip.jpeg

@blu_product.route('/image', methods=["GET"])
@cross_origin()
# @token_required
def fetch_image_route():
    json_data = request.json
    # image = send_file(path , attachment_filename = file)
    images = fetch_image(json_data)
    return json.dumps(images)
