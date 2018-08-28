from flask import *
from extensions import db
import os
import re
import hashlib
import uuid

app = Blueprint('api', __name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def homeApi():
	if 'username' not in session:
		return redirect(url_for("api.loginApi"))

	else:
		if request.method == "GET":
			return render_template("base.html")
		else:
			return "displaying data from database is done here. Calling strava api is done through javascript in html file"		

			# return render_template("base.html")		



@app.route('/login', methods=['POST', 'GET'])
def loginApi():
	if request.method == "GET":
		return render_template("login.html")
	else:
		return("Login page goes here");



@app.route('/create-account', methods=['POST', 'GET'])
def createApi():
	if request.method == "GET":
		return render_template("createAccount.html")
	else:
		vals = request.get_json()
		print(vals['username'])

		confirm = "created account for " + vals['firstname'] + " " + vals['lastname']
		return jsonify(confirm), 203