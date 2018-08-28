from flask import *
from extensions import db
import os

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/', methods=['GET', 'POST'])
def homeApi():
	return render_template("base.html")