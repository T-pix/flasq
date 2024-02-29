from flask import Blueprint,render_template,abort
from jinja2 import TemplateNotFound

home_page = Blueprint('home',__name__)

@home_page.route('/')
def home():
    return render_template('index.html')


