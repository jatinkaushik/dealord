import json
from app import app, db
from app.v1.global_product import *
# from app. import Category
from app.v1.user.model import *
import os
from werkzeug.utils import secure_filename

app.config["IMAGE_UPLOADS"] = "./static/img/"
#-------------------- User Category Check ----------------------

def check_current_user_category_id_global(current_user, cat_id):
    temp = False 
    for i in  current_user.category_global_rel:
        if i.id == cat_id:
            temp = True
    return temp

#--------------------- User SubCategory Check --------------------
# def check_current_user_subcategory_id(current_user, sub_cat_id):
#     sub_cat = Sub_Category.query.filter_by(id='sub_cat_id').first()
#     temp = False
#     if sub_cat:
#         temp = check_current_user_category_id(current_user, sub_cat.category_id)
#     return temp


#============================= Category =========================

#------------------To make a New Category-----------------------

def create_category_global(current_user, json_data): 
    try:
        category_model = GlobalProductCategory(name=json_data['name'], parent=json_data['parent'], user_id=current_user.id) 
        db.session.add(category_model)
        db.session.commit()
        return fetch_category_global()

    except:
        return 'Something Went Wrong'

#-------------------- Delete Category-------------------

def delete_category_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['id']):
            category_search = GlobalProductCategory.query.filter_by(id=json_data['id']).first()
            if not category_search:
                return "category_not_found"
            db.session.delete(category_search)
            db.session.commit()
            return fetch_category_global()
        else:
            return "user_check_fail"    
    except:
        return 'Something Went Wrong'

#--------------------- Edit Category Name ----------------------

def edit_category_global(current_user, json_data):
    try:
        # if check_current_user_category_id_global(current_user, json_data['id']):
            category_search = GlobalProductCategory.query.filter_by(id=json_data['id']).first()
            if not category_search:
                return "category_not_found"
            category_search.name = json_data['name']
            db.session.add(category_search)
            db.session.commit()
            return fetch_category_global()
        # else:
        #     return "user_check_fail"

    except:
        return 'Something Went Wrong'

#----------------------- Fetch Category ------------------

def fetch_category_global():
    # data = current_user.category_global_rel
    data = GlobalProductCategory.query.filter_by(parent=None)
    output = []
    for i in data:
        obj = {
            "id": i.id,
            "name": i.name,
            "child": fetch_sub_category(i.id)
        }
        output.append(obj)
    
    return output
    # check_category = Category.query.filter_by(name=json_data['name']).first()  

    # if check_category:
    #     return "Done"

#--------------Fetch Sub category With parent id---------------

def fetch_sub_category(cat_id):
    parent_check = GlobalProductCategory.query.filter_by(parent=cat_id)
    
    sub_category = []
    for i in parent_check:
        obj = {
            "id" : i.id,
            "name": i.name,
            "user_id": i.user_id,
            "parent_id": i.parent,
            "child": fetch_sub_category(i.id)
        }
        sub_category.append(obj)
        
    return sub_category
            
#==================== Sub Category ==============================

#----------------To make a New Sub_Category---------------

# def create_sub_category(json_data,current_user):
#     try:
#         sub_category_model = GlobalProductCategory(name=json_data['name'], parent_id=json_data['category_id'], user_id=current_user.id) 
#         db.session.add(sub_category_model)
#         db.session.commit()
#         return 'Done'
#     except:
#         return 'Something Went Wrong'  

# #--------------------Fetch Sub Category-------------------

# def fetch_sub_category(current_user, json_data):
#     try:
#         if check_current_user_category_id(current_user, json_data['category_id']):
#             sub_categories = Sub_Category.query.filter_by(category_id = json_data['category_id']).first()
#             if not sub_categories:
#                 return "subcategory_not_found"
#             return json.dumps(sub_categories)
#         else:
#             return "user_check_fail"
#     except:
#         return 'Something Went Wrong'     

# #--------------------Delete Sub Category-------------------

# def delete_sub_category(current_user, json_data):
#     try:
#         if check_current_user_category_id(current_user, json_data['category_id']):
#             subcategory_search = Sub_Category.query.filter_by(id=json_data['id']).first()
#             if not subcategory_search:
#                 return "subcategory_not_found"
#             db.session.delete(subcategory_search)
#             db.session.commit()

#             return 'SubCategory Deleted'
#         else:
#             return "user_check_fail"    
#     except:
#         return 'Something Went Wrong'


# #--------------------- Edit SubCategory Name ----------------------

# def edit_subcategory(current_user, json_data):
#     try:
#         if check_current_user_subcategory_id(current_user, json_data['id']):
#             subcategory_search = Sub_Category.query.filter_by(id=json_data['id']).first()
#             if not subcategory_search:
#                 return "subcategory_not_found"
#             subcategory_search.name = json_data['name']
#             db.session.add(subcategory_search)
#             db.session.commit()
#             return 'SubCategory Edited'
#         else:
#             return "user_check_fail"

#     except:
#         return 'Something Went Wrong'



#===================== Category Features====================

#---------------------- To add features ----------------------

def feature_func_global(json_data): 
    # try:
        for features in json_data:
            feature_model = GlobalProductCategoryFeature(name=features['name'], features_datatype_id=features['features_datatype_id'], category_id=features['category_id'], unit_id=features['unit'], features_groups_id=features['features_groups_id'], recommendation =features['is_recommendation'], feature_required=features['feature_required'],filterable=features['filterable']) 
            db.session.add(feature_model)
            db.session.commit()
            if features['is_recommendation'] == True:
                recommendation_data(features['recommended_options'],feature_model.id,features['features_datatype_id'])
        # cat_id = 
        status = fetch_category_features_global(json_data[0]['category_id'])
        return status 

    # except:
        # return 'Something Went Wrong'


def recommendation_data(add,feature_id,type_id):
    # try:
        for i in add:
            if type_id == 1:
                obj = GlobalProductFeaturesStringRecommended(feature_value = i['value'], feature_id = feature_id)

            if type_id == 2:
                obj = GlobalProductFeaturesIntegerRecommended(feature_value = i['value'], feature_id = feature_id)

            if type_id == 3:
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
        return fetch_features_groups_global(json_data['sub_category_id'])
    except:
        "something went wrong"

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

def delete_features_groups_global(json_data):
    try:
        features_groups = GlobalProductFeaturesGroups.query.filter_by(id=json_data['id']).first()
        db.session.delete(features_groups)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

#---------------- Delete Category Feature -------------------

def delete_category_features_global(current_user, json_data):
    # try:
        # if check_current_user_category_id_global(current_user, json_data['id']):
            category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
            if not category_feature_search:
                return "category_feature_not_found"
            db.session.delete(category_feature_search)
            db.session.commit()
            return 'Feature Delete'
        # else:
        #     return "user_check_fail"
    # except:
    #     return 'Something Went Wrong'

#---------------- Edit Category Feature -------------------

def edit_category_features_global(json_data):
    # try:
        category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
        if not category_feature_search:
            return "category_feature_not_found"
        if 'name' in json_data:
            category_feature_search.name = json_data['name']

        if 'features_datatype_id' in json_data:
            category_feature_search.features_datatype_id = json_data['features_datatype_id']


        if 'category_id' in json_data:
            category_feature_search.category_id = json_data['category_id']
        
        if 'unit' in json_data:
            category_feature_search.unit_id = json_data['unit']

        if 'features_groups_id' in json_data:
            category_feature_search.features_groups_id = json_data['features_groups_id']
        
        if 'filterable' in json_data:
            category_feature_search.filterable = json_data['filterable']
        
        if 'feature_required' in json_data:
            category_feature_search.feature_required = json_data['feature_required']

        if 'is_recommendation' in json_data:
            category_feature_search.recommendation = json_data['is_recommendation']
            # if category_feature_search.recommendation == True:
                
            if category_feature_search.recommendation == False:
                # delete_recommended_features1 = delete_recommended_features(category_feature_search.id)
                delete_recommended_features_values1 = delete_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)

        db.session.add(category_feature_search)
        db.session.commit()
        return 'Category Features Edited'

    # except:
    #     return 'Something Went Wrong'

def edit_category_features_with_check_global(json_data):
    # try:
        category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
        if not category_feature_search:
            return "category_feature_not_found"
        
        if 'name' in json_data:
            if json_data['name'] != category_feature_search.name:
                category_feature_search.name = json_data['name']

        if 'type' in json_data:
            if json_data['type'] != category_feature_search.features_datatype_id:
                delete_recommended_features_values1 = delete_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)
                category_feature_search.features_datatype_id = json_data['type']



        # if 'category_id' in json_data:
        #     if json_data['category_id'] != category_feature_search.category_id:
        #         category_feature_search.category_id = json_data['category_id']
        
        if 'unit' in json_data:
            if json_data['unit'] != category_feature_search.unit_id:
                if category_feature_search.unit_id == False:
                    category_feature_search.unit_id = json_data['unit']
                else:
                    category_feature_search.unit_id = json_data['unit']

        if 'features_groups_id' in json_data:
            if json_data['features_groups_id'] != category_feature_search.features_groups_id:
                category_feature_search.features_groups_id = json_data['features_groups_id']
        
        if 'filterable' in json_data:
            if json_data['filterable'] != category_feature_search.filterable:
                category_feature_search.filterable = json_data['filterable']
        
        if 'feature_required' in json_data:
            if json_data['feature_required'] != category_feature_search.feature_required:
                category_feature_search.feature_required = json_data['feature_required']

        if 'is_recommendation' in json_data:
            recommendation_options = json_data['recommendation_options']
            if json_data['is_recommendation'] != category_feature_search.recommendation:
                category_feature_search.recommendation = json_data['is_recommendation']
                if category_feature_search.recommendation == True:
                    # for add in recommendation_options['add']:
                    add_recommendation = recommendation_data(recommendation_options['add'],category_feature_search.id,category_feature_search.features_datatype_id)   

                if category_feature_search.recommendation == False:
                    # delete_recommended_features1 = delete_recommended_features(category_feature_search.id)
                    delete_recommended_features_values1 = delete_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)
            else:
                if category_feature_search.recommendation == True:
                    if recommendation_options['edit']:
                        for edit in recommendation_options['edit']:
                            edit_recommendation = edit_recommended_particular_value(edit,category_feature_search.features_datatype_id)

                    if recommendation_options['delete']:
                        for delete in recommendation_options['delete']:
                            delete_recommendation = delete_recommended_particular_value(delete,category_feature_search.features_datatype_id)

                    if recommendation_options['add']:
                        # for add in recommendation_options['add']:
                        add_recommendation = recommendation_data(recommendation_options['add'],category_feature_search.id,category_feature_search.features_datatype_id)

        db.session.add(category_feature_search)
        db.session.commit()
        features = fetch_features_global(category_feature_search.id)
        return features

    # except:
    #     return 'Something Went Wrong'

def fetch_features_global(feature_id):
    # try:

        fetch_features = GlobalProductCategoryFeature.query.filter_by(id=feature_id).first()
        # features = []
        
        
        features = {
            "id" : fetch_features.id,
            "name": fetch_features.name,
            "type": fetch_features.features_datatype_id,
            "unit": fetch_features.unit_id if fetch_features.unit_id != None else False,
            "features_groups_id": fetch_features.features_groups_id,
            "feature_required": fetch_features.feature_required,
            "filterable": fetch_features.filterable,
            "is_recommendation": fetch_features.recommendation if fetch_features.recommendation != None else False,
            "recommendation_value": None,
            "recommendation_options": fetch_recommended_features(fetch_features.id, fetch_features.features_datatype_id, fetch_features.recommendation),
            "value": None
            # "features_units": fetch_feature_units_global(fetch_features.unit_id)
        }
            # features.append(obj)
        return features
        
    # except:
    #    return "something went wrong"

def delete_recommended_features(feature_id):
    recommended_features = GlobalProductFeaturesRecommended.query.filter_by(feature_id = feature_id).first()
    db.session.delete(recommended_features)
    db.session.commit()
    return "Done"

def edit_recommended_particular_value(json_data,type_id):
    if type_id == 1:
        recommendation_search = GlobalProductFeaturesStringRecommended.query.filter_by(id=json_data['id']).first()
        if 'feature_id' in json_data:
            recommendation_search.feature_id = json_data['feature_id']

        if 'value' in json_data:
            recommendation_search.feature_value = json_data['value']
    if type_id == 2:
        recommendation_search = GlobalProductFeaturesIntegerRecommended.query.filter_by(id=json_data['id']).first()
        if 'feature_id' in json_data:
            recommendation_search.feature_id = json_data['feature_id']

        if 'value' in json_data:
            recommendation_search.feature_value = json_data['value']
    if type_id == 3:
        recommendation_search = GlobalProductFeaturesDoubleRecommended.query.filter_by(id=json_data['id']).first()
        if 'feature_id' in json_data:
            recommendation_search.feature_id = json_data['feature_id']

        if 'value' in json_data:
            recommendation_search.feature_value = json_data['value']

    db.session.add(recommendation_search)
    db.session.commit()
    return 'done'

def delete_recommended_particular_value(json_data,type_id):
    if type_id == 1:
        recommended_features_value = GlobalProductFeaturesStringRecommended.query.filter_by(id = json_data['id']).first()
        db.session.delete(recommended_features_value)
        db.session.commit()

    if type_id == 2:
        recommended_features_value = GlobalProductFeaturesIntegerRecommended.query.filter_by(id = json_data['id']).first()
        db.session.delete(recommended_features_value)
        db.session.commit()

    if type_id == 3:
        recommended_features_value = GlobalProductFeaturesDoubleRecommended.query.filter_by(id = json_data['id']).first()
        db.session.delete(recommended_features_value)
        db.session.commit()

    return 'done'

def delete_recommended_features_values(feature_id,type_id):
    
    if type_id == 1:
        recommended_features_values = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    if type_id == 2:
        recommended_features_values = GlobalProductFeaturesIntegerRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    if type_id == 3:
        recommended_features_values = GlobalProductFeaturesDoubleRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    return "Done"


def fetch_recommended_features(feature_id, data_type ,recommendation):
    try:
        
        if recommendation:
            if data_type == 1:
                feature_value_check = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)

            if data_type == 2:
                feature_value_check = GlobalProductFeaturesIntegerRecommended.query.filter_by(feature_id = feature_id)

            if data_type == 3:
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
                "unit": i.unit_id if i.unit_id != None else False,
                "features_groups_id": i.features_groups_id,
                "feature_required": i.feature_required,
                "filterable": i.filterable,
                "is_recommendation": i.recommendation if i.recommendation != None else False,
                "recommendation_value": None,
                "recommendation_options": fetch_recommended_features(i.id, i.features_datatype_id, i.recommendation),
                "value": None
                # "features_units": fetch_feature_units_global(i.unit_id)
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
                "unit": i.unit_id if i.unit_id != None else False,
                "features_groups_id": i.features_groups_id,
                "feature_required": i.feature_required,
                "filterable": i.filterable,
                "is_recommendation": i.recommendation if i.recommendation != None else False,
                "recommendation_value": None,
                "recommendation_options": fetch_recommended_features(i.id, i.features_datatype_id, i.recommendation),
                "value": None
                # "features_units": fetch_feature_units_global(i.unit_id)
            }
            cat_features["features"].append(obj)
        cat_features["features_groups"] = fetch_features_groups_global(cat_id)
        return cat_features

#----------------- Add Datatype ---------------------------- 

def feature_datatypefunc_global(json_data):
    try:
        feature_type = GlobalProductFeaturesDatatype(name=json_data['name'])
        db.session.add(feature_type)
        db.session.commit()
        return "Done"
    except:
        return 'Something Went Wrong'

def fetch_datatypefunc_global(json_data):
    try:
        features_datatype = []
        fetch_features_datatype = GlobalProductFeaturesDatatype.query.all()
        for i in fetch_features_datatype:
            obj = {
                "value" : i.id,
                "label": i.name
            }
            features_datatype.append(obj)
        return features_datatype
    except:
        return "Something Went Wrong"

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

#===================== Product =====================================

#------------------ Add Product ----------------------------

def add_product_global(json_data):
    # for i in json_data["product"]:
        addproduct = GlobalProductProducts(varient = json_data['varient'])
        db.session.add(addproduct)
        db.session.commit()
        product_id = addproduct.id
        return product_id

# def add_product_global(json_data):
#     try:
#         for i in json_data['product']:
#             addproduct = GlobalProductProductsVarient(name = i['name'],category_id = i['categoy_id'])
#             db.session.add(addproduct)
#             db.session.commit()
#             return addproduct.id
#     except:
#         return 'Something Went Wrong'
        
#------------------- Add Product ------------------------

def add_product_data_global(json_data):
    try:
        # temp = json_data['product']
        addproduct = GlobalProductProductsVarient(name = json_data['name'],category_id = json_data['category_id'])
        db.session.add(addproduct)
        db.session.commit()
        product_varient_id = addproduct.id
    
        # return "Done"
        return json.dumps(product_varient_id)
        # return json.dumps(temp)
    except:
        return 'Something Went Wrong'    


#-----------------------Product Features-----------------------
# def product_features(json_data):
#     # try:
#         product = json_data['product']
#         product_id = add_product_global(product)
#         addproduct = GlobalProductProductsVarient(name = product['name'],category_id = product['category_id'],product_id = product_id,country_of_origin = product['country_of_origin'],description_of_products = product['description_of_products'],is_product_features_added = product['is_product_features_added'])
#         db.session.add(addproduct)
#         db.session.commit()
#         product_varient_id = addproduct.id
#         for i in json_data['features']:
#             if i['is_recommendation'] == True:
#                 if i['type'] == 1:
#                     obj = GlobalProductFeaturesRecommended(feature_id = i['id'], string_seleted_id = i['value'], product_varient_id = product_varient_id)

#                 if i['type'] == 2:
#                     obj = GlobalProductFeaturesRecommended(feature_id = i['id'], integer_seleted_id= i['value'], product_varient_id = product_varient_id)

#                 if i['type'] == 3:
#                     obj = GlobalProductFeaturesRecommended(feature_id = i['id'], double_seleted_id= i['value'], product_varient_id = product_varient_id)
#                 db.session.add(obj)
#                 db.session.commit()
#             else:
#                 if i['type'] == 1:
#                     obj = GlobalProductFeaturesString(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

#                 if i['type'] == 2:
#                     obj = GlobalProductFeaturesInteger(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

#                 if i['type'] == 4:
#                     obj = GlobalProductFeaturesDate(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

#                 if i['type'] == 5:
#                     obj = GlobalProductFeaturesBoolean(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)   

#                 if i['type'] == 3:
#                     obj = GlobalProductFeaturesDouble(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)
                    
#                 db.session.add(obj)
#                 db.session.commit()

#         for varient in json_data['varient_features']:
#             # varient_features_id = add_varient_global(product_id,varient)
#             add_varient_data = GlobalProductVarientFeatures(feature_id=varient['feature_id'], product_id = product_id)
#             db.session.add(add_varient_data) 
#             db.session.commit()
        
#         id_s = {
#             "product_varient_id":product_varient_id,
#             "product_id" : product_id
#         }
#         return id_s
    # except:
    #     return 'Something Went Wrong'



def add_product_with_image(image,json_data):
    # try:
        product = json.loads(json_data['json'])
        product_id = add_product_global(product)
        addproduct = GlobalProductProductsVarient(name = product['name'],category_id = product['category_id'],product_id = product_id,country_of_origin = product['country_of_origin'],description_of_products = product['description_of_products'])
        db.session.add(addproduct)
        db.session.commit()
        product_varient_id = addproduct.id
        for key in image:
            file = image.get(key)
            order = int(json_data.get(key))
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            path = app.config["IMAGE_UPLOADS"]+filename
            # print("path: ", path)
            image_data = GlobalProductProductsImage(product_varient_id = product_varient_id,image_path = path, order = order)
            db.session.add(image_data)
            db.session.commit()

        id_s = {
            "product_varient_id":product_varient_id,
            "product_id" : product_id
        }
        return id_s
    # except:
    #     return 'Something Went Wrong'

def product_features(json_data,product_varient_id):
    for i in json_data['features']:
        if i['is_recommendation'] == True:
            if i['type'] == 1:
                obj = GlobalProductFeaturesRecommended(feature_id = i['id'], string_seleted_id = i['value'], product_varient_id = product_varient_id)

            if i['type'] == 2:
                obj = GlobalProductFeaturesRecommended(feature_id = i['id'], integer_seleted_id= i['value'], product_varient_id = product_varient_id)

            if i['type'] == 3:
                obj = GlobalProductFeaturesRecommended(feature_id = i['id'], double_seleted_id= i['value'], product_varient_id = product_varient_id)
            db.session.add(obj)
            db.session.commit()
        else:
            if i['type'] == 1:
                obj = GlobalProductFeaturesString(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

            if i['type'] == 2:
                obj = GlobalProductFeaturesInteger(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

            if i['type'] == 4:
                obj = GlobalProductFeaturesDate(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

            if i['type'] == 5:
                obj = GlobalProductFeaturesBoolean(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)   

            if i['type'] == 3:
                obj = GlobalProductFeaturesDouble(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)
                
            db.session.add(obj)
            db.session.commit()
        
    fetch_required_features = GlobalProductCategoryFeature.query.filter_by(category_id=json_data['category_id'],feature_required=True)
    for feature in fetch_required_features:
        if feature.recommendation == True:
            if feature.features_datatype_id == 1:
                value_available = GlobalProductFeaturesRecommended.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 2:
                value_available = GlobalProductFeaturesRecommended.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 3:
                value_available = GlobalProductFeaturesRecommended.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
        else:
            if feature.features_datatype_id == 1:
                value_available = GlobalProductFeaturesString.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 2:
                value_available = GlobalProductFeaturesInteger.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 3:
                value_available = GlobalProductFeaturesDouble.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 4:
                value_available = GlobalProductFeaturesDate.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 5:
                value_available = GlobalProductFeaturesBoolean.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
    else:
        is_product_features_added = True
        
        # for varient in json_data['varient_features']:
        #     # varient_features_id = add_varient_global(product_id,varient)
        #     add_varient_data = GlobalProductVarientFeatures(feature_id=varient['feature_id'], product_id = product_id)
        #     db.session.add(add_varient_data) 
        #     db.session.commit()

#--------------------- To Add Varient ----------------------------

def add_varient_global(json_data):
    try:
        fetch_product = GlobalProductProducts.query.filter_by(id = json_data['product_id']).first()
        fetch_product.varient = True
        db.session.add(fetch_product)
        db.session.commit()
        for feature_id in json_data['feature_ids']:
            add_varient_data = GlobalProductVarientFeatures(feature_id=feature_id, product_id = json_data['product_id'])
            db.session.add(add_varient_data)
            db.session.commit()
            # varient_features_id = add_varient_data.id
        return "done"
    except:
        return 'Something Went Wrong'



#-----------------------Fetch Product -------------------------

def fetch_product_global(current_user,json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['category_id']):   
            fetch_product_obj = GlobalProductProductsVarient.query.filter_by(id=json_data['product_varient_id']).first()

            if not fetch_product_obj:
                return "product_not_found"

            return "to_decide" 
        else:
            return "user_check_fail"
    except:
        return 'Something Went Wrong'


#--------------------Extra Features For Product -----------------

def extra_features_global(json_data):
    try:
        add_features = GlobalProductFeaturesExtra(name=json_data['name'], feature_type_id=json_data['feature_type_id'],product_varient_id = json_data['product_varient_id'],units=json_data['units'])
        db.session.add(add_features) 
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'


def feature_units_types_global(json_data):
    try:
        add_features_units_types = GlobalProductFeaturesUnitsTypes(name = json_data['name_types'])
        db.session.add(add_features_units_types)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

# def feature_units_global(json_data):
#     try:
#         add_features_units = GlobalProductFeaturesUnits(name = json_data['name'],units_id = json_data['units_id'])
#         db.session.add(add_features_units)
#         db.session.commit()
#         return "done"
#     except:
        # return 'Something Went Wrong'

def fetch_feature_units_global():
    # try:
        fetch_units = GlobalProductFeaturesUnitsTypes.query.all()
        units =[]
        for unit in fetch_units:
            obj = {
                "value": unit.id,
                "label": unit.name,
                "selected_unit": unit.selected_unit,
                "units": fetch_add_units(unit.id)
            }
            units.append(obj)
        return units
    # except:
        # return "Something went Wrong"


def add_units(json_data):
    try:
        for unit in json_data:       
            units_arrey = GlobalProductFeaturesUnits(name = unit['name'], units_type_id = unit['units_type_id'], order = unit['order'])
            db.session.add(units_arrey)
            db.session.commit()
        return "done"
    except:
        return "Something went Wrong"

def fetch_add_units(units_type_id):
    try:
        fetch_units_obj = GlobalProductFeaturesUnits.query.filter_by(units_type_id = units_type_id)
        units = []
        for unit in fetch_units_obj:
            obj = {
                "value": unit.id,
                "label": unit.name,
                "order": unit.order,
                "exp": unit.exp,
                "exp_value": unit.value,
                "units_type_id": unit.units_type_id,
            }
            units.append(obj)
        return units
    except:
        return "Something went Wrong"    
# def add_data_of_recommendation(json_data):
#     try:
#         recommendation_data = GlobalProductFeaturesRecommended()

def upload_image(image,json_data):
    # try:
        product = json.loads(json_data['json'])
        for key in image:
            file = image.get(key)
            order = int(json_data.get(key))
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            path = app.config["IMAGE_UPLOADS"]+filename
            # print("path: ", path)
            image_data = GlobalProductProductsImage(product_varient_id = product['product_id'],image_path = path, order = order)
            db.session.add(image_data)
            db.session.commit()
        return "done"
    # except:
    #     return "Something went Wrong" 

def fetch_image(json_data):
    try:
        fetch_image_obj = GlobalProductProductsImage.query.filter_by(product_varient_id = json_data['product_varient_id'])
        images =[]
        for image in fetch_image_obj:
            obj = {
                "id": image.id,
                "product_varient_id": image.product_varient_id,
                "image_path": "http://127.0.0.1:5000/v1/globalproduct"+image.image_path,
                "order": image.order
            }
            images.append(obj)
        return images
    except:
        return "Something went Wrong" 
