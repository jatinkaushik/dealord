import json
from app import app, db
from app.v1.general_data.datatypes import *

def feature_datatypefunc_global(json_data):
    try:
        feature_type = GeneralDataDatatype(name=json_data['name'], abbreviation = json_data['abbreviation'])
        db.session.add(feature_type)
        db.session.commit()
        return "Done"
    except:
        return 'Something Went Wrong'

def fetch_datatypefunc_global(json_data):
    try:
        features_datatype = []
        fetch_features_datatype = GeneralDataDatatype.query.all()
        for i in fetch_features_datatype:
            obj = {
                "id" : i.id,
                "label": i.name,
                "value":i.abbreviation
            }
            features_datatype.append(obj)
        return features_datatype
    except:
        return "Something Went Wrong"

