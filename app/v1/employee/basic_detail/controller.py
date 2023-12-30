import json
from app import app, db
from app.v1.employee.basic_detail import *


def employee_basic(json_data):
    # try:
        employee_basic_detail = Employee(name=json_data['name'], email=json_data['email'],company_id=json_data['company_id'],employee_id=json_data['employee_id'], primary_phone_no=json_data['primary_phone_no'])
        db.session.add(employee_basic_detail)
        db.session.commit()
        return 'Done'
    # except:
        # return 'Something Went Wrong'

def fetch_employee_basic(json_data):
    try:
        fetch_employee_basic_detail = Employee.query.filter_by(employee_id=json_data['employee_id'])
        output = []
        for i in fetch_employee_basic_detail :
            obj = {
                "id": i.id,
                "name": i.name,
                "company_id":i.company_id,
                "employee_id": i.employee_id,
                "primary_phone_no": i.primary_phone_no,
                "email": i.email
            }
            output.append(obj)
        return output
    except:
        return 'Something Went Wrong'

def edit_employee_basic(json_data):
    # try:
        edit_employee_basic_detail = Employee.query.filter_by(employee_id=json_data['employee_id']).first()
        if 'name' in json_data:
            edit_employee_basic_detail.name = json_data['name']

        if 'employee_id1' in json_data:
            edit_employee_basic_detail.employee_id = json_data['employee_id1']

        if 'primary_phone_no' in json_data:
            edit_employee_basic_detail.primary_phone_no = json_data['primary_phone_no']
        
        if 'email' in json_data:
            edit_employee_basic_detail.email = json_data['email']
        
        db.session.add(edit_employee_basic_detail)
        db.session.commit()
        
        return "done"    
    # except:
    #     return 'Something Went Wrong'

def delete_employee_basic(json_data):
    try:
        edit_employee_basic_detail = Employee.query.filter_by(employee_id=json_data['employee_id']).first()
        db.session.delete(edit_employee_basic_detail)
        db.session.commit()
        return 'Employee Deleted'
    except:
        return 'Something Went Wrong'

def addpersonal_detail(json_data):
    try:
        personal_detail = EmployeePersonalDetail(employee_id1=json_data['employee_id'], alternate_phone_no=json_data['alternate_phone_no'], father_name=json_data['father_name'], date_of_birth=['date_of_birth'],pan_number=['pan_number'],gender=['gender'])
        db.session.add(personal_detail)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

def fetch_personal_detail(json_data):
    try:
        persional_detail_fetch = EmployeePersonalDetail.query.filter_by(employee_id=json_data['employee_id']).first()

        output = []
        for i in persional_detail_fetch :
            obj = {
                "id": i.id,
                "father_name": i.father_name,
                "employee_id": i.employee_id,
                "alternate_phone_no": i.alternate_phone_no,
                "date_of_birth": i.date_of_birth,
                "pan_number": i.pan_number,
                "gender": i.gender
            }
            output.append(obj)
        return output
    except:
        return 'Something Went Wrong'

def edit_personal_detail(json_data):
    try:
        edit_emplyee_personal_detail = EmployeePersonalDetail.query.filter_by(employee_id=json_data['employee_id']).first()

        if json_data['father_name']:
            edit_emplyee_personal_detail.name = json_data['father_name']

        if json_data['employee_id']:
            edit_emplyee_personal_detail.employee_id = json_data['employee_id']

        if json_data['alternate_phone_no']:
            edit_emplyee_personal_detail.primary_phone_no = json_data['alternate_phone_no']
        
        if json_data['date_of_birth']:
            edit_emplyee_personal_detail.email = json_data['date_of_birth']

        if json_data['pan_number']:
            edit_emplyee_personal_detail.email = json_data['pan_number']

        if json_data['gender']:
            edit_emplyee_personal_detail.email = json_data['gender']
                   
        db.session.add(edit_emplyee_personal_detail)
        db.session.commit()
        
        return "done"    
    except:
        return 'Something Went Wrong'

def delete_employee_personal_detail(json_data):
    try:
        delete_personal_detail = EmployeePersonalDetail.query.filter_by(employee_id=json_data['employee_id']).first()
        db.session.delete(delete_personal_detail)
        db.session.commit()
        return 'deleted'
    except:
        return 'Something Went Wrong'

def address_detail(json_data):
    try:
        address_column = Address(employee_id1=json_data['employee_id'], address_line1=json_data['address_line1'], address_line2=json_data['address_line2'], city=json_data['city'], state=json_data['state'], country=json_data['country'], pin_code=json_data['pin_code']) 
        db.session.add(address_column)
        db.session.commit()
        return 'Done'
    except:
        return 'Something Went Wrong'

# def fetch_address(json_data):
#     try:
#         fetch_