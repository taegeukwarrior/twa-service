from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Afif/Project/Weekend Project/Taegeuk Warrior Chat Bot/service/twa.db'
db = SQLAlchemy(app)

from twa_app.students.view import students
from twa_app.home.view import landing
app.register_blueprint(students)
app.register_blueprint(landing)

db.create_all()
