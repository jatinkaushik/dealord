import json
from app import app, db
from app.v1.general_data.countries import *
from app.v1.general_data.countries.countries_data import countries

def fetch_country():
    data = Countries.query.all()
    output = []
    for i in data:
        obj = {
            "value": i.id,
            "label": i.name
        }
        output.append(obj)
    
    return output

def add_country():
    db.session.execute(countries)
    db.session.commit()
    return