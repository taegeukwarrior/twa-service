from flask import Blueprint

landing = Blueprint('landing',__name__)

@landing.route('/')
@landing.route('/home')

def home():
    return '<h1>V1 API LANDING PAGE</h1>'
