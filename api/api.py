from flask import *
from extensions import db
import os
import re
import hashlib
import uuid

app = Blueprint('api', __name__, template_folder='templates')

@app.route('/', methods=['GET'])
def homeApi():
	if 'username' not in session:
		return render_template("login.html")

	else:
		return "displaying data from database is done here. Calling strava api is done through javascript in html file"		




@app.route('/login', methods=['POST', 'GET'])
def loginApi():
	return "login page here"



@app.route('/create-account', methods=['POST', 'GET'])
def createApi():
	return render_template("createAccount.html")