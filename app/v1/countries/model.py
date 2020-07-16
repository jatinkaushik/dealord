from app import db
from app.v1.global_product import *

class Countries(db.Model):
    __tablename__ = 'countries'
    id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name',db.String(100))
    iso3 = db.Column('iso3',db.String(5))
    iso2 = db.Column('iso2',db.String(5))
    phonecode = db.Column('phonecode',db.String(200))
    capital = db.Column('capital',db.String(200))
    currency = db.Column('currency',db.String(200))
    native = db.Column('native',db.String(200))
    emoji = db.Column('emoji',db.String(200))
    emojiU = db.Column('emojiU',db.String(200))
    created_at = db.Column('created_at',db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at',db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    flag = db.Column('flag',db.Boolean)
    wikiDataId = db.Column('wikiDataId',db.String(200))
    # states_rel = db.relationship('States', backref='countries')
    # cities_rel = db.relationship('Cities', backref='countries')
    global_product_rel = db.relationship('GlobalProductProductsVarient', backref='countries')

# class States(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     country_id = db.Column(db.Integer,db.ForeignKey('countries.id'))
#     country_code = db.Column(db.String(5))
#     fips_code = db.Column(db.String(200))
#     iso2 = db.Column(db.String(5))
#     created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
#     updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
#     flag = db.Column(db.Boolean)
#     wikiDataId = db.Column(db.String(200))  
#     states_rel = db.relationship('Cities', backref='states') 

# class Cities(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     state_id = db.Column(db.Integer,db.ForeignKey('states.id'))
#     state_code = db.Column(db.String(5))
#     country_id = db.Column(db.Integer,db.ForeignKey('countries.id'))
#     country_code = db.Column(db.String(5))
#     latitude = db.Column(db.Float)
#     longitude = db.Column(db.Float)
#     created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
#     updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
#     flag = db.Column(db.Boolean)
#     wikiDataId = db.Column(db.String(200))
