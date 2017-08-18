import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from twa_app import db, app
from twa_app.students.model import Students

students = Blueprint('students',__name__)

class StudentsView(MethodView):

    def get(self, twa_stu_id=None, page=1):
        if not twa_stu_id:
            stus = Students.query.paginate(page, 10).items
            res = {}
            for stu in stus:
                res[stu.twa_stu_id] = {
                    'name' : stu.twa_stu_name,
                    'address' : stu.twa_stu_address,
                    'phone' : str(stu.twa_stu_phone)
                }
        else:
            stu = Students.query.filter_by(twa_stu_id=twa_stu_id).first()
            if not stu:
                abort(404)
            res = {
                'name' : stu.twa_stu_name,
                'address' : stu.twa_stu_address,
                'phone' : str(stu.twa_stu_phone)
            }

        mess = {
            "messages" : [
                {
                    "text" : "Coba Aja Cuk!"
                }
            ],
            "set_attributes" : {
                "nama" : "Afif",
                "alamat" : "pati",
                "usia" : "20",
                "nohp" : "081333501063"
            }
        }

        return jsonify(mess)

    def post(self):
        twa_stu_name = request.form.get('name')
        twa_stu_age = request.form.get('age')
        twa_stu_address = request.form.get('alamat')
        twa_stu_phone = request.form.get('phone')
        twa_stu_photo = request.form.get('photo')
        stu = Students(twa_stu_name, twa_stu_age, twa_stu_address, twa_stu_phone, twa_stu_photo)
        db.session.add(stu)
        db.session.commit()

        return jsonify({stu.twa_stu_id :{
            'name' : stu.twa_stu_name,
            'age' : stu.twa_stu_age,
            'alamat' : stu.twa_stu_address,
            'phone' : stu.twa_stu_phone,
            'photo' : stu.twa_stu_photo
        }})


students_view = StudentsView.as_view('students_view')
app.add_url_rule(
    '/students/', view_func=students_view, methods=['GET', 'POST']
)

app.add_url_rule(
    '/students/<int:twa_stu_id>', view_func=students_view, methods=['GET']
)
