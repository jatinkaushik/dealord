import json
from app import app, db
from app.v1.product import Category, Sub_Category, Sub_Category_Feature, Features_Datatype, Products , Integer_Features, Date_Features, Boolean_Features, String_Features, Double_Features,Extra_Features,Varient
# from app. import Category
from app.v1.user.model import *

#-------------------- User Category Check ----------------------

def check_current_user_category_id(current_user, cat_id):
    temp = False 
    for i in  current_user.category_rel:
        if i.id == cat_id:
            temp = True
    return temp

#--------------------- User SubCategory Check --------------------
def check_current_user_subcategory_id(current_user, sub_cat_id):
    sub_cat = Sub_Category.query.filter_by(id='sub_cat_id').first()
    temp = False
    if sub_cat:
        temp = check_current_user_category_id(current_user, sub_cat.category_id)
    return temp


#============================= Category =========================

#------------------To make a New Category-----------------------

def create_category(current_user, json_data): 
    try:
        category_model = Category(name=json_data['name'], parent=json_data['parent'], user_id=current_user.id) 
        db.session.add(category_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

#-------------------- Delete Category-------------------

def delete_category(current_user, json_data):
    try:
        if check_current_user_category_id(current_user, json_data['id']):
            category_search = Category.query.filter_by(id=json_data['id']).first()
            if not category_search:
                return "category_not_found"
            db.session.delete(category_search)
            db.session.commit()
            return 'Category Deleted'
        else:
            return "user_check_fail"    
    except:
        return 'Something Went Wrong'

#--------------------- Edit SubCategory Name ----------------------

def edit_category(current_user, json_data):
    try:
        if check_current_user_category_id(current_user, json_data['id']):
            category_search = Category.query.filter_by(id=json_data['id']).first()
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

def fetch_category(current_user):
    data = current_user.category_rel
    output = []
    for i in data:
        obj = {
            "id": i.id,
            "name": i.name
        }
        output.append(obj)
    
    return output
    # check_category = Category.query.filter_by(name=json_data['name']).first()  

    # if check_category:
    #     return "Done"

#==================== Sub Category ==============================

#----------------To make a New Sub_Category---------------

def create_sub_category(json_data):
    try:
        sub_category_model = Sub_Category(name=json_data['name'], category_id=json_data['category_id']) 
        db.session.add(sub_category_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'  

#--------------------Fetch Sub Category-------------------

def fetch_sub_category(current_user, json_data):
    try:
        if check_current_user_category_id(current_user, json_data['category_id']):
            sub_categories = Sub_Category.query.filter_by(category_id = json_data['category_id']).first()
            if not sub_categories:
                return "subcategory_not_found"
            return json.dumps(sub_categories)
        else:
            return "user_check_fail"
    except:
        return 'Something Went Wrong'     

#--------------------Delete Sub Category-------------------

def delete_sub_category(current_user, json_data):
    try:
        if check_current_user_category_id(current_user, json_data['category_id']):
            subcategory_search = Sub_Category.query.filter_by(id=json_data['id']).first()
            if not subcategory_search:
                return "subcategory_not_found"
            db.session.delete(subcategory_search)
            db.session.commit()

            return 'SubCategory Deleted'
        else:
            return "user_check_fail"    
    except:
        return 'Something Went Wrong'


#--------------------- Edit SubCategory Name ----------------------

def edit_subcategory(current_user, json_data):
    try:
        if check_current_user_subcategory_id(current_user, json_data['id']):
            subcategory_search = Sub_Category.query.filter_by(id=json_data['id']).first()
            if not subcategory_search:
                return "subcategory_not_found"
            subcategory_search.name = json_data['name']
            db.session.add(subcategory_search)
            db.session.commit()
            return 'SubCategory Edited'
        else:
            return "user_check_fail"

    except:
        return 'Something Went Wrong'



#===================== Sub Category Features====================

#---------------------- To add features ----------------------

def feature_func(json_data): 
    try:
        feature_model = Sub_Category_Feature(name=json_data['name'], features_datatype_id=json_data['feature_type'], sub_category_id=json_data['sub_category_id'], units=json_data['units']) 
        db.session.add(feature_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

#---------------- Delete Sub Category Feature -------------------

def delete_sub_category_features(current_user, json_data):
    try:
        if check_current_user_subcategory_id(current_user, json_data['sub_category_id']):
            sub_category_features = Sub_Category_Feature.query.filter_by(sub_category_id=json_data['sub_category_id']).first()
            if not subcategory_feature_search:
                return "subcategory_feature_not_found"
            db.session.delete(sub_category_features)
            db.session.commit()
            return 'Feature Delete'
        else:
            return "user_check_fail"
    except:
        return 'Something Went Wrong'

#---------------- Edit Sub Category Feature -------------------

def edit_subcategory_features(current_user, json_data):
    try:
        if check_current_user_subcategory_id(current_user, json_data['id']):
            subcategory_feature_search = Sub_Category_Feature.query.filter_by(id=json_data['id']).first()
            if not subcategory_feature_search:
                return "subcategory_feature_not_found"
            subcategory_feature_search.name = json_data['name']
            db.session.add(subcategory_feature_search)
            db.session.commit()
            return 'SubCategory Feature Edited'
        else:
            return "user_check_fail"

    except:
        return 'Something Went Wrong'

#-------------------- SubCategory Data Features ---------------------

def fetch_sub_category_features(current_user, json_data):
    try:
        if check_current_user_subcategory_id(current_user, json_data['sub_category_id']):
            check_type = Sub_Category_Feature.query.filter_by(sub_category_id=json_data['sub_category_id']).first()
            subcat_features = {
                "features": []
            }
            for i in check_type:
                obj = {
                    "id" : i.id,
                    "name": i.name,
                    "type": i.features_datatype_id,
                    "units": i.units
                }
                subcat_features["features"].append(obj)
            return json.dumps(subcat_features)
        else: 
            return "user_check_fail"
        
    except:
        "something went wrong"

#----------------- Add Datatype ---------------------------- 

def feature_datatypefunc(json_data):
    try:
        feature_type = Features_Datatype(name=json_data['name'])
        db.session.add(feature_type)
        db.session.commit()
        return "Done"
    except:
        "something went wrong"

#-------------------- Integer Datatype Features ---------------

def add_integer_feature(json_data):
    try:
        add_integer = Integer_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_integer)
        db.session.commit()
        return add_integer
    except: 
        "something went wrong"

#-------------------- String Datatype Features ---------------

def add_string_feature(json_data):
    try:
        add_string = String_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_string)
        db.session.commit()
        return add_string
    except: 
        "something went wrong"

#-------------------- Double Datatype Features ---------------

def add_double_feature(json_data):
    try:
        add_double = Double_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_double)
        db.session.commit()
        return add_double
    except:
        "something went wrong"

#-------------------- Boolean Datatype Features ---------------

def add_boolean_feature(json_data):
    try:
        add_boolean = Boolean_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_boolean)
        db.session.commit()
        return add_boolean
    except:
        "something went wrong"        

#-------------------- Datetime Datatype Features ---------------

def add_date_features(json_data):
    try:
        add_date = Date_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_date)
        db.session.commit()
        return add_date
    except:
        "something went wrong"

#===================== Product =====================================

#------------------ Add Product ----------------------------

def add_product(json_data):
    for i in json_data['product']:
        try:
            addproduct = Products(name = i['name'],sub_category_id = i['sub_categoy_id'])
            db.session.add(addproduct)
            db.session.commit()
            return addproduct.id
        except:
            "something went wrong"
        
#-------------------Product Features ------------------------

def add_product_data(json_data):
    try:
        temp = json_data['product']
        addproduct = Products(name = temp['name'],sub_category_id = temp['sub_category_id'])
        db.session.add(addproduct)
        db.session.commit()
        product_id = addproduct.id

        for i in json_data['features']:
            if i['type'] == 1:
                obj = String_Features(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)

            if i['type'] == 2:
                obj = Integer_Features(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)

            if i['type'] == 3:
                obj = Date_Features(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)

            if i['type'] == 5:
                obj = Boolean_Features(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)   

            if i['type'] == 6:
                obj = Double_Features(feature_value = i['feature_value'], feature_id = i['feature_id'], product_id = product_id)
                
            db.session.add(obj)
            db.session.commit()
        return json.dumps(product_id)
        # return json.dumps(temp)
    except:
        "something went wrong"    

#-----------------------Fetch Product -------------------------

def fetch_product(current_user,json_data):
    try:
        if check_current_user_subcategory_id(current_user, json_data['sub_category_id']):   
            fetch_product_obj = Products.query.filter_by(id=json_data['product_id']).first()

            if not fetch_product_obj:
                return "product_not_found"

            return "to_decide" 
        else:
            return "user_check_fail"
    except:
        "something went wrong"


#--------------------Extra Features For Product -----------------

def extra_features(json_data):
    try:
        add_features = Extra_Features(name=json_data['name'], feature_type_id=json_data['feature_type_id'],product_id = json_data['product_id'],units=json_data['units'])
        db.session.add(add_features) 
        db.session.commit()
        return "done"
    except:
        "something went wrong"    

#--------------------- To Add Varient ----------------------------

def add_varient(json_data):
    try:
        add_varient_data = Varient(sub_category_feature_id=json_data['sub_category_feature_id'], product_id = json_data['product_id'])
        db.session.add(add_varient_data) 
        db.session.commit()
        return "done"
    except:
        "something went wrong" 