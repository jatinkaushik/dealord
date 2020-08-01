from app import db

class GeneralDataUnitsTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class GeneralDataUnits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    units_type_id = db.Column(db.Integer, db.ForeignKey('general_data_units_types.id'))
    exp = db.Column(db.String(5))
    value = db.Column(db.Float)
    order = db.Column(db.Integer)

