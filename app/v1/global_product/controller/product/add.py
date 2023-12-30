import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model.product.product import *
from app.v1.global_product.model1 import *
import os
from werkzeug.utils import secure_filename

#------------------ Add Product ----------------------------

def add_product_global(json_data):
    # for i in json_data["product"]:
        addproduct = GlobalProductProducts(varient = json_data['varient'])
        db.session.add(addproduct)
        db.session.commit()
        product_id = addproduct.id
        return product_id

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
            path = path[1:]
            # print("path: ", path)
            image_data = GlobalProductProductsImage(product_varient_id = product_varient_id,image_path = path, order = order)
            db.session.add(image_data)
            db.session.commit()

        id_s = {
            "product_varient_id":product_varient_id,
            "product_id" : product_id
        }
        return id_s

def product_features(json_data,product_varient_id):
    for i in json_data['features']:
        if i['is_recommendation'] == True:
            if i['type'] == 'str':
                obj = GlobalProductFeaturesRecommended(feature_id = i['id'], string_seleted_id = i['value'], product_varient_id = product_varient_id)

            if i['type'] == 'int':
                obj = GlobalProductFeaturesRecommended(feature_id = i['id'], integer_seleted_id= i['value'], product_varient_id = product_varient_id)

            if i['type'] == 'float':
                obj = GlobalProductFeaturesRecommended(feature_id = i['id'], double_seleted_id= i['value'], product_varient_id = product_varient_id)
            db.session.add(obj)
            db.session.commit()
        else:
            if i['type'] == 'str':
                obj = GlobalProductFeaturesString(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

            if i['type'] == 'int':
                obj = GlobalProductFeaturesInteger(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

            if i['type'] == 'datetime':
                obj = GlobalProductFeaturesDate(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)

            if i['type'] == 'boolean':
                obj = GlobalProductFeaturesBoolean(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)   

            if i['type'] == 'float':
                obj = GlobalProductFeaturesDouble(feature_value = i['value'], feature_id = i['id'], product_varient_id = product_varient_id)
                
            db.session.add(obj)
            db.session.commit()
        
    fetch_required_features = GlobalProductCategoryFeature.query.filter_by(category_id=json_data['category_id'],feature_required=True)
    for feature in fetch_required_features:
        if feature.recommendation == True:
            if feature.features_datatype_id == 'str':
                value_available = GlobalProductFeaturesRecommended.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 'int':
                value_available = GlobalProductFeaturesRecommended.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 'float':
                value_available = GlobalProductFeaturesRecommended.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
        else:
            if feature.features_datatype_id == 'str':
                value_available = GlobalProductFeaturesString.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 'int':
                value_available = GlobalProductFeaturesInteger.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 'float':
                value_available = GlobalProductFeaturesDouble.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 'datetime':
                value_available = GlobalProductFeaturesDate.query.filter_by(feature_id=feature.id,product_varient_id=product_varient_id).first()
                if not value_available:
                    break
            if feature.features_datatype_id == 'boolean':
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
