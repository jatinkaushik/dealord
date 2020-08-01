import json
from app import app, db
from app.v1.general_data.datatypes import *

def feature_datatypefunc_global(json_data):
    try:
        feature_type = GeneralDataDatatype(name=json_data['name'])
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
                "value" : i.id,
                "label": i.name
            }
            features_datatype.append(obj)
        return features_datatype
    except:
        return "Something Went Wrong"

def feature_units_types_global(json_data):
    try:
        add_features_units_types = GeneralDataUnitsTypes(name = json_data['name_types'])
        db.session.add(add_features_units_types)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_feature_units_global():
    # try:
        fetch_units = GeneralDataUnitsTypes.query.all()
        units =[]
        for unit in fetch_units:
            obj = {
                "value": unit.id,
                "label": unit.name,
                # "selected_unit": unit.selected_unit,
                "units": fetch_add_units(unit.id)
            }
            units.append(obj)
        return units
    # except:
        # return "Something went Wrong"


def add_units(json_data):
    try:
        for unit in json_data:       
            units_arrey = GeneralDataUnits(name = unit['name'], units_type_id = unit['units_type_id'], order = unit['order'],exp =unit['exp'], value = unit['value'])
            db.session.add(units_arrey)
            db.session.commit()
        return "done"
    except:
        return "Something went Wrong"

def fetch_add_units(units_type_id):
    try:
        fetch_units_obj = GeneralDataUnits.query.filter_by(units_type_id = units_type_id)
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