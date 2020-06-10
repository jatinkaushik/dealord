import json
from app import app, db
from app.v1.global_product import Category_Global, Category_Feature_Global, Features_Datatype_Global, Products_Global , Integer_Features_Global, Date_Features_Global, Boolean_Features_Global, String_Features_Global, Double_Features_Global,Extra_Features_Global,Varient_Global, Features_Groups_Global
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
        category_model = Category_Global(name=json_data['name'], parent=json_data['parent'], user_id=current_user.id) 
        db.session.add(category_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

#-------------------- Delete Category-------------------

def delete_category_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['id']):
            category_search = Category_Global.query.filter_by(id=json_data['id']).first()
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
            category_search = Category_Global.query.filter_by(id=json_data['id']).first()
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
    data = Category_Global.query.filter_by(parent=None)
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
    parent_check = Category_Global.query.filter_by(parent=cat_id)
    
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

# def create_sub_category(json_data):
#     try:
#         sub_category_model = Sub_Category(name=json_data['name'], category_id=json_data['category_id']) 
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
    try:
        feature_model = Category_Feature_Global(name=json_data['name'], features_datatype_id=json_data['features_datatype_id'], category_id=json_data['category_id'], unit=json_data['units'], features_groups_id=json_data['features_groups_id']) 
        db.session.add(feature_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

#----------------Features Groups Function -------------------
def features_groups_global(json_data):
    try:
        features_group = Features_Groups_Global(name=json_data['name'])
        db.session.add(features_group)
        db.session.commit()
        return "Done"
    except:
        "something went wrong"
#---------------- Delete Category Feature -------------------

def delete_category_features_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['id']):
            category_feature_search = Category_Feature_Global.query.filter_by(sub_category_id=json_data['sub_category_id']).first()
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

def edit_category_features_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['id']):
            category_feature_search = Category_Feature_Global.query.filter_by(id=json_data['id']).first()
            if not category_feature_search:
                return "category_feature_not_found"
            category_feature_search.name = json_data['name']
            db.session.add(category_feature_search)
            db.session.commit()
            return 'Category Feature Edited'
        else:
            return "user_check_fail"

    except:
        return 'Something Went Wrong'

#-------------------- Category Data Features ---------------------

def fetch_category_features_global(current_user, json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['category_id']):
            check_type = Category_Feature_Global.query.filter_by(category_id=json_data['category_id'])
            cat_features = {
                "features": []
            }
            for i in check_type:
                obj = {
                    "id" : i.id,
                    "name": i.name,
                    "type": i.features_datatype_id,
                    "units": i.unit
                }
                cat_features["features"].append(obj)
            return json.dumps(cat_features)
        else: 
            return "user_check_fail"
        
    except:
       return "something went wrong"

#----------------- Add Datatype ---------------------------- 

def feature_datatypefunc_global(json_data):
    try:
        feature_type = Features_Datatype_Global(name=json_data['name'])
        db.session.add(feature_type)
        db.session.commit()
        return "Done"
    except:
        return 'Something Went Wrong'

#-------------------- Integer Datatype Features ---------------

def add_integer_feature_global(json_data):
    try:
        add_integer = Integer_Features_Global(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_integer)
        db.session.commit()
        return add_integer
    except: 
        return 'Something Went Wrong'

#-------------------- String Datatype Features ---------------

def add_string_feature_global(json_data):
    try:
        add_string = String_Features_Global(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_string)
        db.session.commit()
        return add_string
    except: 
        return 'Something Went Wrong'
#-------------------- Double Datatype Features ---------------

def add_double_feature_global(json_data):
    try:
        add_double = Double_Features_Global(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_double)
        db.session.commit()
        return add_double
    except:
        return 'Something Went Wrong'

#-------------------- Boolean Datatype Features ---------------

def add_boolean_feature_global(json_data):
    try:
        add_boolean = Boolean_Features_Global(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_boolean)
        db.session.commit()
        return add_boolean
    except:
        return 'Something Went Wrong'        

#-------------------- Datetime Datatype Features ---------------

def add_date_features_global(json_data):
    try:
        add_date = Date_Features_Global(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
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
            addproduct = Products_Global(name = i['name'],category_id = i['categoy_id'])
            db.session.add(addproduct)
            db.session.commit()
            return addproduct.id
        except:
            return 'Something Went Wrong'
        
#------------------- Add Product ------------------------

def add_product_data_global(json_data):
    try:
        # temp = json_data['product']
        addproduct = Products_Global(name = json_data['name'],category_id = json_data['category_id'])
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
    # try:
        product_id = json_data["product_id"]
        for i in json_data['features']:
            if i['type'] == 1:
                obj = String_Features_Global(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)

            if i['type'] == 2:
                obj = Integer_Features_Global(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)

            if i['type'] == 4:
                obj = Date_Features_Global(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)

            if i['type'] == 5:
                obj = Boolean_Features_Global(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)   

            if i['type'] == 3:
                obj = Double_Features_Global(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)
                
            db.session.add(obj)
            db.session.commit()
        return json.dumps(product_id)
    # except:
    #     return 'Something Went Wrong'   

#-----------------------Fetch Product -------------------------

def fetch_product_global(current_user,json_data):
    try:
        if check_current_user_category_id_global(current_user, json_data['category_id']):   
            fetch_product_obj = Products_Global.query.filter_by(id=json_data['product_id']).first()

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
        add_features = Extra_Features_Global(name=json_data['name'], feature_type_id=json_data['feature_type_id'],product_id = json_data['product_id'],units=json_data['units'])
        db.session.add(add_features) 
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

#--------------------- To Add Varient ----------------------------

def add_varient_global(json_data):
    try:
        add_varient_data = Varient_Global(sub_category_feature_id=json_data['sub_category_feature_id'], product_id = json_data['product_id'])
        db.session.add(add_varient_data) 
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'