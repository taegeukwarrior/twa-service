from twa_app import db

class Students(db.Model):
    twa_stu_id = db.Column(db.Integer, primary_key = True)
    twa_stu_name = db.Column(db.String(200))
    twa_stu_age = db.Column(db.Integer)
    twa_stu_address = db.Column(db.String(200))
    twa_stu_phone = db.Column(db.String(14))
    twa_stu_photo = db.Column(db.String)

    def __init__(self, twa_stu_name, twa_stu_address, twa_stu_age, twa_stu_phone, twa_stu_photo):
        self.twa_stu_name = twa_stu_name
        self.twa_stu_age = twa_stu_age
        self.twa_stu_address = twa_stu_address
        self.twa_stu_phone = twa_stu_phone
        self.twa_stu_photo = twa_stu_photo

    def __repr__(self):
        return '<Student %d>' % self.twa_stu_id
