import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model1 import *


def fetch_features_groups_global(cat_id):
    try:
        cat_features = []
        features_group = GlobalProductFeaturesGroups.query.filter_by(sub_category_id=cat_id)
        for i in features_group:
            obj = {
                "id" : i.id,
                "name": i.name,
                "order": i.order
            }
            cat_features.append(obj)
        return cat_features
    except:
        return "something went wrong"

def fetch_recommended_features(feature_id, data_type ,recommendation):
    try:
        
        if recommendation:
            if data_type == 'str':
                feature_value_check = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)

            if data_type == 'int':
                feature_value_check = GlobalProductFeaturesIntegerRecommended.query.filter_by(feature_id = feature_id)

            if data_type == 'float':
                feature_value_check = GlobalProductFeaturesDoubleRecommended.query.filter_by(feature_id = feature_id)
            
            obj = []
            for i in feature_value_check:
                obj1 ={
                    "value" : i.id,
                    "label": i.feature_value
                }
                obj.append(obj1)
            return obj  
        else:
            return []
    except:
        return  'Something Went Wrong'       

#-------------------- Category Data Features ---------------------

def fetch_category_features_global(cat_id):
    # try:

        fetch_features = GlobalProductCategoryFeature.query.filter_by(category_id=cat_id)
        features = []
        
        for i in fetch_features:
            obj = {
                "id" : i.id,
                "name": i.name,
                "type": i.features_datatype_id,
                "category_id": i.category_id,
                "unit": i.unit_types_id if i.unit_types_id != None else False,
                "groups_id": i.features_groups_id,
                "is_required": i.feature_required,
                "filterable": i.filterable,
                "is_recommendation": i.recommendation if i.recommendation != None else False,
                "recommendation_value": None,
                "recommendation_options": fetch_recommended_features(i.id, i.features_datatype_id, i.recommendation),
                "value": None
                # "features_units": fetch_feature_units_global(i.unit_types_id)
            }
            features.append(obj)
        return features
        
    # except:
    #    return "something went wrong"
    
def fetch_category_with_groups_features_global(cat_id):
    # try:

        fetch_features = GlobalProductCategoryFeature.query.filter_by(category_id=cat_id)
        
        cat_features = {
            "features": [],
            "features_groups": []
        }
        
        for i in fetch_features:
            obj = {
                "id" : i.id,
                "name": i.name,
                "type": i.features_datatype_id,
                "category_id": i.category_id,
                "unit": i.unit_types_id if i.unit_types_id != None else False,
                "groups_id": i.features_groups_id,
                "is_required": i.feature_required,
                "filterable": i.filterable,
                "is_recommendation": i.recommendation if i.recommendation != None else False,
                "recommendation_value": None,
                "recommendation_options": fetch_recommended_features(i.id, i.features_datatype_id, i.recommendation),
                "value": None
                # "features_units": fetch_feature_units_global(i.unit_types_id)
            }
            cat_features["features"].append(obj)
        cat_features["features_groups"] = fetch_features_groups_global(cat_id)
        return cat_features

def fetch_features_groups_global(cat_id):
    try:
        cat_features = []
        features_group = GlobalProductFeaturesGroups.query.filter_by(sub_category_id=cat_id)

        for i in features_group:
            obj = {
                "id" : i.id,
                "name": i.name,
                "order": i.order
            }
            cat_features.append(obj)
        return cat_features
    except:
        return "something went wrong"
