from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id = db.Column(db.Integer, unique= True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(40))
    primary_phone_no = db.Column(db.String(15))
    employee_personal_detail_rel = db.relationship('EmployeePersonalDetail', backref = 'employee')
    address_rel = db.relationship('Address', backref = 'employee')
    department_rel = db.relationship('Department', backref = 'employee')
    designation_rel = db.relationship('Designation', backref = 'employee')

class EmployeePersonalDetail(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id1 = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    alternate_phone_no = db.Column(db.String(15))
    father_name = db.Column(db.String(30))
    date_of_birth = db.Column(db.DateTime)
    pan_number = db.Column(db.String(20))
    gender = db.Column(db.String(10))

class Address(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id1 = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    country = db.Column(db.String(30))
    pin_code = db.Column(db.Integer)

class ShiftTime(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    shift_name = db.Column(db.String(30))
    shift_time_start = db.Column(db.DateTime)
    shift_time_end = db.Column(db.DateTime)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id1 = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    department_name = db.Column(db.String(30))

class Designation(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    employee_id1 = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    designation_name = db.Column(db.String(30))

