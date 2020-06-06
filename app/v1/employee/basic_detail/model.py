from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    email = db.Column(db.String(40))
    primary_phone_no = db.Column(db.String(15))
    employee_personal_detail = db.relationship('EmployeePersonalDetail', backref='employee')

class EmployeePersonalDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer,  db.ForeignKey('employee.employee_id'))
    alternate_phone_no = db.Column(db.String(15))
    father_name = db.Column(db.String(30))
    date_of_birth = db.Column(db.DateTime)
    pan_number = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    
    
    