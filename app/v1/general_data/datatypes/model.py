from app import db

class GeneralDataDatatype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    abbreviation = db.Column(db.String(10),unique=True)
    # category_features_rel = db.relationship('GlobalProductCategoryFeature', backref='general_data_datatype')
