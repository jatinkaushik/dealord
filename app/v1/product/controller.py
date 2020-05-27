import json
from app import app, db
from app.v1.product import Category, Sub_Category, Sub_Category_Feature, Features_Datatype, Products , Integer_Features, Date_Features, Boolean_Features, String_Features, Double_Features,Extra_Features,Varient
# from app. import Category

#To make a New Category
def create_category(json_data): 
    try:
        category_model = Category(name=json_data['name'], parent=json_data['parent'], user_id=json_data['user_id']) 
        db.session.add(category_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

 #To make a New Sub_Category
def create_sub_category(json_data):
    try:
        sub_category_model = Sub_Category(name=json_data['name'], category_id=json_data['category_id']) 
        db.session.add(sub_category_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'  

def fetch_category():
    data = Category.query.all()
    output = []
    for i in data:
        obj = {
            "name": i.name
        }
        output.append(obj)
    
    return output
    # check_category = Category.query.filter_by(name=json_data['name']).first()  

    # if check_category:
    #     return "Done"

def fetch_sub_category(json_data):
    try:
        check_sub_category = Sub_Category.query.filter_by(id = json_data['id']).first()
        db.session.add(check_sub_category)
        db.session.commit()
        return json.dumps(check_sub_category)

    except:
        return 'Something Went Wrong'     

# To add features
def feature_func(json_data): 
    try:
        feature_model = Sub_Category_Feature(name=json_data['name'], features_datatype_id=json_data['feature_type'], sub_category_id=json_data['sub_category_id'], units=json_data['units']) 
        db.session.add(feature_model)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

# Features DataType
def get_sub_category_features(json_data):
    # try:
    check_type = Sub_Category_Feature.query.filter_by(sub_category_id=json_data['sub_category_id'])
    subcat_features = {
        "features": []
    }
    for i in check_type:
        obj = {
            "name": i.name,
            "type": i.features_datatype_id,
            "units": i.units
        }
        subcat_features["features"].append(obj)
    return json.dumps(subcat_features)
    # except:
    #     "something went wrong"

def feature_datatypefunc(json_data):
    try:
        feature_type = Features_Datatype(name=json_data['name'])
        db.session.add(feature_type)
        db.session.commit()
        return "Done"
    except:
        "something went wrong"

def add_product(json_data):
    for i in json_data['product']:
        try:
            addproduct = Products(name = i['name'],sub_category_id = i['sub_categoy_id'])
            db.session.add(addproduct)
            db.session.commit()
            return addproduct.id
        except:
            "something went wrong"
        
    

def add_integer_feature(json_data):
    try:
        add_integer = Integer_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_integer)
        db.session.commit()
        return add_integer
    except: 
        "something went wrong"

def add_string_feature(json_data):
    try:
        add_string = String_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_string)
        db.session.commit()
        return add_string
    except: 
        "something went wrong"

def add_double_feature(json_data):
    try:
        add_double = Double_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_double)
        db.session.commit()
        return add_double
    except:
        "something went wrong"

def add_boolean_feature(json_data):
    try:
        add_boolean = Boolean_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_boolean)
        db.session.commit()
        return add_boolean
    except:
        "something went wrong"        

def add_date_features(json_data):
    try:
        add_date = Date_Features(feature_value = json_data['feature_value'], feature_id = json_data['feature_id'], product_id=json_data['product_id'])
        db.session.add(add_date)
        db.session.commit()
        return add_date
    except:
        "something went wrong"

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


def extra_features(json_data):
    try:
        add_features = Extra_Features(name=json_data['name'], feature_type_id=json_data['feature_type_id'],product_id = json_data['product_id'],units=json_data['units'])
        db.session.add(add_features) 
        db.session.commit()
        return "done"
    except:
        "something went wrong"    

def add_varient(json_data):
    try:
        add_varient_data = Varient(sub_category_feature_id=json_data['sub_category_feature_id'], product_id = json_data['product_id'])
        db.session.add(add_varient_data) 
        db.session.commit()
        return "done"
    except:
        "something went wrong" 