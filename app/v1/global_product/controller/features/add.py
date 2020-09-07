import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model1 import *
from app.v1.global_product.controller.features.fetch import *

def feature_func_global(json_data): 
    # try:
        for features in json_data:
            feature_model = GlobalProductCategoryFeature(name=features['name'], features_datatype_id=features['type'], category_id=features['category_id'], unit_types_id=features['unit'], features_groups_id=features['groups_id'], recommendation =features['is_recommendation'], feature_required=features['is_required'],filterable=features['filterable']) 
            db.session.add(feature_model)
            db.session.commit()
            if features['is_recommendation'] == True:
                recommendation_data(features['recommended_options'],feature_model.id,features['type'])
        # cat_id = 
        status = fetch_category_features_global(json_data[0]['category_id'])
        return status

    # except:
        # return 'Something Went Wrong'


def recommendation_data(add,feature_id,type_id):
    # try:
        for i in add:
            if type_id == 'str':
                obj = GlobalProductFeaturesStringRecommended(feature_value = i['value'], feature_id = feature_id)
                db.session.add(obj)
                db.session.commit()

            if type_id == 'int':
                obj = GlobalProductFeaturesIntegerRecommended(feature_value = i['value'], feature_id = feature_id)
                db.session.add(obj)
                db.session.commit()

            if type_id == 'float':
                obj = GlobalProductFeaturesDoubleRecommended(feature_value = i['value'], feature_id = feature_id)
                db.session.add(obj)
                db.session.commit()
        return "done"
    # except:
    #     return 'Something Went Wrong'

#----------------Features Groups Function -------------------
def features_groups_global(json_data):
    try:
        features_group = GlobalProductFeaturesGroups(name=json_data['name'], sub_category_id=json_data['sub_category_id'],order=json_data['order'])
        db.session.add(features_group)
        db.session.commit()
        # return fetch_features_groups_global(json_data['sub_category_id'])
        return "done"
    except:
        "something went wrong"

#-------------------- Integer Datatype Features ---------------

def add_integer_feature_global(json_data):
    try:
        add_integer = GlobalProductFeaturesInteger(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_varient_id=json_data['product_varient_id'])
        db.session.add(add_integer)
        db.session.commit()
        return add_integer
    except: 
        return 'Something Went Wrong'

#-------------------- String Datatype Features ---------------

def add_string_feature_global(json_data):
    try:
        add_string = GlobalProductFeaturesString(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_varient_id=json_data['product_varient_id'])
        db.session.add(add_string)
        db.session.commit()
        return add_string
    except: 
        return 'Something Went Wrong'
#-------------------- Double Datatype Features ---------------

def add_double_feature_global(json_data):
    try:
        add_double = GlobalProductFeaturesDouble(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_varient_id=json_data['product_varient_id'])
        db.session.add(add_double)
        db.session.commit()
        return add_double
    except:
        return 'Something Went Wrong'

#-------------------- Boolean Datatype Features ---------------

def add_boolean_feature_global(json_data):
    try:
        add_boolean = GlobalProductFeaturesBoolean(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_varient_id=json_data['product_varient_id'])
        db.session.add(add_boolean)
        db.session.commit()
        return add_boolean
    except:
        return 'Something Went Wrong'        

#-------------------- Datetime Datatype Features ---------------

def add_date_features_global(json_data):
    try:
        add_date = GlobalProductFeaturesDate(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_varient_id=json_data['product_varient_id'])
        db.session.add(add_date)
        db.session.commit()
        return add_date
    except:
        return 'Something Went Wrong'