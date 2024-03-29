from app import db
from app.v1.user.model import *
from app.v1.company.model import *

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    parent = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    # sub_category_rel = db.relationship('Sub_Category', backref='category')
    sub_category_features_rel = db.relationship('Category_Feature', backref='category')
    products_rel = db.relationship('Products', backref='category')

# class Sub_Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     sub_category_features_rel = db.relationship('Sub_Category_Feature', backref='sub__category')
#     products_rel = db.relationship('Products', backref='sub__category')

class Features_Datatype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category_features_rel = db.relationship('Category_Feature', backref='features__datatype')
    

class Category_Feature(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    features_datatype_id = db.Column(db.Integer, db.ForeignKey('features__datatype.id'))
    unit = db.Column(db.Integer, nullable=True)
    string_features_rel = db.relationship('String_Features', backref='category__feature')
    integer_features_rel = db.relationship('Integer_Features', backref='category__feature')
    double_features_rel = db.relationship('Double_Features', backref='category__feature')
    datetime_features_rel = db.relationship('Date_Features', backref='category__feature')
    boolean_features_rel = db.relationship('Boolean_Features', backref='category__feature')
    varient_rel = db.relationship('Varient', backref='category__feature')


class Products(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    company_id = db.Column(db.Integer,db.ForeignKey('company_company.id'))
    string_features_rel = db.relationship('String_Features', backref='products')
    integer_features_rel = db.relationship('Integer_Features', backref='products')
    double_features_rel = db.relationship('Double_Features', backref='products')
    datetime_features_rel = db.relationship('Date_Features', backref='products')
    boolean_features_rel = db.relationship('Boolean_Features', backref='products')
    Extra_features_rel = db.relationship('Extra_Features', backref='products')
    varient_rel = db.relationship('Varient', backref='products')

class String_Features(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
class Integer_Features(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

class Double_Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class Date_Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.DateTime)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

class Boolean_Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Boolean)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

class Extra_Features(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    feature_type_id = db.Column(db.Integer)
    units = db.Column(db.Integer)

class Varient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category_feature_id = db.Column(db.Integer, db.ForeignKey('category__feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
