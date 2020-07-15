import json
from app import app, db
from app.v1.countries import *

def fetch_country(json_data):
    data = Countries.query.all()
    output = []
    for i in data:
        obj = {
            "id": i.id,
            "name": i.name
        }
        output.append(obj)
    
    return output