import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model.product.product import *
from app.v1.global_product.model.features.features import *
from app.v1.global_product.model1 import *

def fetch_product_varient(json_data):
    # try:
        fetch_product_varient = GlobalProductProductsVarient.query.filter_by(id = json_data['product_varient_id']).first()
        fetch_product_varient_image = fetch_image(json_data)

        product_varient = {
            "id" : fetch_product_varient.id,
            "name": fetch_product_varient.name,
            "category_id": fetch_product_varient.category_id,
            "product_id": fetch_product_varient.product_id,
            "country_of_origin": fetch_product_varient.country_of_origin,
            "description_of_products": fetch_product_varient.description_of_products,
            "is_product_features_added": fetch_product_varient.is_product_features_added,
            "product_live": fetch_product_varient.product_live,
            "product_approve": fetch_product_varient.product_approve,
            "master_product": fetch_product_varient.master_product
            
        }

        if not product_varient['master_product']:
            features = []
            fetch_product_varient_features_string_values = GlobalProductFeaturesString.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_string = []
            for feature in fetch_product_varient_features_string_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_string.append(obj)
            features.append(features_string)
            fetch_product_varient_features_integer_values = GlobalProductFeaturesInteger.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_integer = []
            for feature in fetch_product_varient_features_integer_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_integer.append(obj)
            features.append(features_integer)

            fetch_product_varient_features_double_values = GlobalProductFeaturesDouble.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_double = []
            for feature in fetch_product_varient_features_double_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_double.append(obj)
            features.append(features_double)

            fetch_product_varient_features_datetime_values = GlobalProductFeaturesDate.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_datetime = []
            for feature in fetch_product_varient_features_datetime_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_datetime.append(obj)
            features.append(features_datetime)

            fetch_product_varient_features_boolean_values = GlobalProductFeaturesBoolean.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_boolean = []
            for feature in fetch_product_varient_features_boolean_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_boolean.append(obj)
            features.append(features_boolean)
        else:
            fetch_varient_features = GlobalProductVarientFeatures.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features = []
            fetch_product_varient_features_string_values = GlobalProductFeaturesString.query.filter_by(product_varient_id = product_varient['master_product'])
            features_string = []
            for feature in fetch_product_varient_features_string_values:
                count = 0
                for varient_feature in fetch_varient_features:
                    if feature.feature_id == varient_feature.feature_id:
                        count += 1
                if count != 0:
                    fetch_product_varient_features_values = GlobalProductFeaturesString.query.filter_by(product_varient_id = json_data['product_varient_id'],feature_id = feature.feature_id).first()
                    fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                    obj = {
                        "id" : fetch_product_varient_features_values.id,
                        "name": fetch_product_varient_features.name,
                        "feature_id": fetch_product_varient_features_values.feature_id,
                        "feature_value": fetch_product_varient_features_values.feature_value
                    }
                    features_string.append(obj)
                else:
                    fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                    obj = {
                        "id" : feature.id,
                        "name": fetch_product_varient_features.name,
                        "feature_id": feature.feature_id,
                        "feature_value": feature.feature_value
                    }
                    features_string.append(obj)
            features.append(features_string)

            fetch_product_varient_features_integer_values = GlobalProductFeaturesInteger.query.filter_by(product_varient_id = product_varient['master_product'])
            features_integer = []
            for feature in fetch_product_varient_features_integer_values:
                count = 0
                for varient_feature in fetch_varient_features:
                    if feature.feature_id == varient_feature.feature_id:
                        count += 1
                if count != 0:
                    fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                    obj = {
                        "id" : feature.id,
                        "name": fetch_product_varient_features.name,
                        "feature_id": feature.feature_id,
                        "feature_value": feature.feature_value
                    }
                features_integer.append(obj)
            features.append(features_integer)

            fetch_product_varient_features_double_values = GlobalProductFeaturesDouble.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_double = []
            for feature in fetch_product_varient_features_double_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_double.append(obj)
            features.append(features_double)

            fetch_product_varient_features_datetime_values = GlobalProductFeaturesDate.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_datetime = []
            for feature in fetch_product_varient_features_datetime_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_datetime.append(obj)
            features.append(features_datetime)

            fetch_product_varient_features_boolean_values = GlobalProductFeaturesBoolean.query.filter_by(product_varient_id = json_data['product_varient_id'])
            features_boolean = []
            for feature in fetch_product_varient_features_boolean_values:
                fetch_product_varient_features = GlobalProductCategoryFeature.query.filter_by(id = feature.feature_id).first()
                obj = {
                    "id" : feature.id,
                    "name": fetch_product_varient_features.name,
                    "feature_id": feature.feature_id,
                    "feature_value": feature.feature_value
                }
                features_boolean.append(obj)
            features.append(features_boolean)



        product_varient_with_features = {
            'product_varient': product_varient,
            'features': features,
            'product_varient_image':fetch_product_varient_image
        }
        return product_varient_with_features
    # except:
    #     return 'Something Went Wrong'

def fetch_image(json_data):
    try:
        fetch_image_obj = GlobalProductProductsImage.query.filter_by(product_varient_id = json_data['product_varient_id'])
        images =[]
        for image in fetch_image_obj:
            path = image.image_path
            # path = path[1:]
            obj = {
                "id": image.id,
                "product_varient_id": image.product_varient_id,
                "image_path": "http://127.0.0.1:5000/v1/globalproduct"+path,
                "order": image.order
            }
            images.append(obj)
        return images
    except:
        return "Something went Wrong" 