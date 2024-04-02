from app import app, db
from models import Student, Major
import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of students first_name, last_name, major_id, birth_date, is_honors
    students = [
        {'student_id': '1', 'first_name': 'Robert', 'last_name':'Smith', 'major_id':3,
            'birth_date': dt.datetime(2007, 6, 1), 'is_honors':1,'student_email':'jimpaidas@umd.edu'},
        {'student_id': '2', 'first_name': 'Leo', 'last_name': 'Van Munching', 'major_id':6,
         'birth_date': dt.datetime(2008, 3, 24), 'is_honors': 0, 'student_email':'zoepaidas@umd.edu'},
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            major_id=each_student["major_id"], birth_date=each_student["birth_date"],
                            is_honors=each_student["is_honors"], student_email=each_student["student_email"])
        db.session.add(a_student)
        db.session.commit()



