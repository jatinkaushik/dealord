import json
from app import app, db
from app.v1.global_product import *
# from app. import Category
from app.v1.user.model import *

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
        return 'Done'
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
            return 'Category Deleted'
        else:
            return "user_check_fail"    
    except:
        return 'Something Went Wrong'

#--------------------- Edit Category Name ----------------------

def edit_category_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['id']):
            category_search = GlobalProductCategory.query.filter_by(id=json_data['id']).first()
            if not category_search:
                return "category_not_found"
            category_search.name = json_data['name']
            db.session.add(category_search)
            db.session.commit()
            return 'Category Edited'
        else:
            return "user_check_fail"

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
            feature_model = GlobalProductCategoryFeature(name=features['name'], features_datatype_id=features['features_datatype_id'], category_id=features['category_id'], unit_id=features['unit'], features_groups_id=features['features_groups_id'], recommendation =features['is_recommendation']) 
            db.session.add(feature_model)
            db.session.commit()
            if features['is_recommendation'] == True:
                status = recommendation_data(features,feature_model.id)
            else:
                status = "done"
        return status 

    # except:
        # return 'Something Went Wrong'


def recommendation_data(features,feature_id):
    # try:
        for i in features['recommended_options']:
            if features['features_datatype_id'] == 1:
                obj = GlobalProductFeaturesStringRecommended(feature_value = i['value'], feature_id = feature_id)

            if features['features_datatype_id'] == 2:
                obj = GlobalProductFeaturesIntegerRecommended(feature_value = i['value'], feature_id = feature_id)

            if features['features_datatype_id'] == 3:
                obj = GlobalProductFeaturesDoubleRecommended(feature_value = i['value'], feature_id = feature_id)
            db.session.add(obj)
            db.session.commit()
        return "done"
    # except:
    #     return 'Something Went Wrong'


#----------------Features Groups Function -------------------
def features_groups_global(json_data):
    try:
        features_group = GlobalProductFeaturesGroups(name=json_data['name'], sub_category_id=json_data['sub_category_id'])
        db.session.add(features_group)
        db.session.commit()
        return "Done"
    except:
        "something went wrong"

def fetch_features_groups_global(cat_id):
    try:
        cat_features = []
        features_group = GlobalProductFeaturesGroups.query.filter_by(sub_category_id=cat_id)
        for i in features_group:
            obj = {
                "id" : i.id,
                "name": i.name
            }
            cat_features.append(obj)
        return cat_features
    except:
        return "something went wrong"

#---------------- Delete Category Feature -------------------

def delete_category_features_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['id']):
            category_feature_search = GlobalProductCategoryFeature.query.filter_by(sub_category_id=json_data['sub_category_id']).first()
            if not category_feature_search:
                return "category_feature_not_found"
            db.session.delete(category_feature_search)
            db.session.commit()
            return 'Feature Delete'
        else:
            return "user_check_fail"
    except:
        return 'Something Went Wrong'

#---------------- Edit Category Feature -------------------

def edit_category_features_global(json_data):
    # try:
        category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
        # if not category_feature_search:
        #     return "category_feature_not_found"
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
        
        if 'is_recommendation' in json_data:
            category_feature_search.recommendation = json_data['is_recommendation']
            if category_feature_search.recommendation == False:
                # delete_recommended_features1 = delete_recommended_features(category_feature_search.id)
                delete_recommended_features_values1 = delete_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)

        db.session.add(category_feature_search)
        db.session.commit()
        return 'Category Features Edited'

    # except:
    #     return 'Something Went Wrong'

def delete_recommended_features(feature_id):
    recommended_features = GlobalProductFeaturesRecommended.query.filter_by(feature_id = feature_id).first()
    db.session.delete(recommended_features)
    db.session.commit()
    return "Done"

def delete_recommended_features_values(feature_id,type_id):
    
    if type_id == 1:
        recommended_features_values = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    if type_id == 2:
        recommended_features_values = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    if type_id == 3:
        recommended_features_values = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)
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
                "is_recommendation": i.recommendation if i.recommendation != None else False,
                "recommendation_value": None,
                "recommendation_options": fetch_recommended_features(i.id, i.features_datatype_id, i.recommendation),
                "value": None
                # "features_units": fetch_feature_units_global(i.unit_id)
            }
            cat_features["features"].append(obj)
        cat_features["features_groups"] = fetch_features_groups_global(cat_id)
        return cat_features
        
        
    # except:
    #    return "something went wrong"

#----------------- Add Datatype ---------------------------- 

def feature_datatypefunc_global(json_data):
    try:
        feature_type = GlobalProductFeaturesDatatype(name=json_data['name'])
        db.session.add(feature_type)
        db.session.commit()
        return "Done"
    except:
        return 'Something Went Wrong'

#-------------------- Integer Datatype Features ---------------

def add_integer_feature_global(json_data):
    try:
        add_integer = GlobalProductFeaturesInteger(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_integer)
        db.session.commit()
        return add_integer
    except: 
        return 'Something Went Wrong'

#-------------------- String Datatype Features ---------------

def add_string_feature_global(json_data):
    try:
        add_string = GlobalProductFeaturesString(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_string)
        db.session.commit()
        return add_string
    except: 
        return 'Something Went Wrong'
#-------------------- Double Datatype Features ---------------

def add_double_feature_global(json_data):
    try:
        add_double = GlobalProductFeaturesDouble(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_double)
        db.session.commit()
        return add_double
    except:
        return 'Something Went Wrong'

#-------------------- Boolean Datatype Features ---------------

def add_boolean_feature_global(json_data):
    try:
        add_boolean = GlobalProductFeaturesBoolean(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_boolean)
        db.session.commit()
        return add_boolean
    except:
        return 'Something Went Wrong'        

#-------------------- Datetime Datatype Features ---------------

def add_date_features_global(json_data):
    try:
        add_date = GlobalProductFeaturesDate(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_date)
        db.session.commit()
        return add_date
    except:
        return 'Something Went Wrong'

#===================== Product =====================================

#------------------ Add Product ----------------------------

def add_product_global(json_data):
    for i in json_data['product']:
        try:
            addproduct = GlobalProducts(name = i['name'],category_id = i['categoy_id'])
            db.session.add(addproduct)
            db.session.commit()
            return addproduct.id
        except:
            return 'Something Went Wrong'
        
#------------------- Add Product ------------------------

def add_product_data_global(json_data):
    try:
        # temp = json_data['product']
        addproduct = GlobalProducts(name = json_data['name'],category_id = json_data['category_id'])
        db.session.add(addproduct)
        db.session.commit()
        product_id = addproduct.id
    
        # return "Done"
        return json.dumps(product_id)
        # return json.dumps(temp)
    except:
        return 'Something Went Wrong'    


#-----------------------Product Features-----------------------
def product_features(json_data):
    try:
        product = json_data['product']
        addproduct = GlobalProductProducts(name = product['name'],category_id = product['category_id'])
        db.session.add(addproduct)
        db.session.commit()
        product_id = addproduct.id
        for i in json_data['features']:
            if i['is_recommendation'] == True:
                if i['type'] == 1:
                    obj = GlobalProductFeaturesRecommended(feature_id = i['id'], string_seleted_id = i['value'], product_id = product_id)

                if i['type'] == 2:
                    obj = GlobalProductFeaturesRecommended(feature_id = i['id'], integer_seleted_id= i['value'], product_id = product_id)

                if i['type'] == 3:
                    obj = GlobalProductFeaturesRecommended(feature_id = i['id'], double_seleted_id= i['value'], product_id = product_id)
                db.session.add(obj)
                db.session.commit()
            else:
                if i['type'] == 1:
                    obj = GlobalProductFeaturesString(feature_value = i['value'], feature_id = i['id'], product_id = product_id)

                if i['type'] == 2:
                    obj = GlobalProductFeaturesInteger(feature_value = i['value'], feature_id = i['id'], product_id = product_id)

                if i['type'] == 4:
                    obj = GlobalProductFeaturesDate(feature_value = i['value'], feature_id = i['id'], product_id = product_id)

                if i['type'] == 5:
                    obj = GlobalProductFeaturesBoolean(feature_value = i['value'], feature_id = i['id'], product_id = product_id)   

                if i['type'] == 3:
                    obj = GlobalProductFeaturesDouble(feature_value = i['value'], feature_id = i['id'], product_id = product_id)
                    
                db.session.add(obj)
                db.session.commit()
        return json.dumps(product_id)
    except:
        return 'Something Went Wrong'





#-----------------------Fetch Product -------------------------

def fetch_product_global(current_user,json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['category_id']):   
            fetch_product_obj = GlobalProducts.query.filter_by(id=json_data['product_id']).first()

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
        add_features = GlobalProductFeaturesExtra(name=json_data['name'], feature_type_id=json_data['feature_type_id'],product_id = json_data['product_id'],units=json_data['units'])
        db.session.add(add_features) 
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

#--------------------- To Add Varient ----------------------------

def add_varient_global(json_data):
    try:
        add_varient_data = GlobalProductVarient(sub_category_feature_id=json_data['sub_category_feature_id'], product_id = json_data['product_id'])
        db.session.add(add_varient_data) 
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
        units ={
            "feature_units": []
        }
        for unit in fetch_units:
            obj = {
                "id": unit.id,
                "name": unit.name
            }
            units["feature_units"].append(obj)
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
# def add_data_of_recommendation(json_data):
#     try:
#         recommendation_data = GlobalProductFeaturesRecommended()