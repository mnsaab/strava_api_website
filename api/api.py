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
		vals = request.get_json()
		# print(vals['username'])

		username = vals['username']
		password = vals['password']

		# For when the password is encrypted in the database, I need to do some encrypting and decrypting to match the passwords 

		cur = db.cursor()
		
		query = "SELECT * FROM accounts WHERE username=\"" + username + "\""
		cur.execute(query)
		dbData = cur.fetchone()

		if (dbData == None):
			return jsonify("This username cannot be found, if you don't have an account, please make one. Otherwise, please try again"), 403

		if (dbData['password'] != password):
			return jsonify("This password does not match with the given username, please try again"), 403

		session['username'] = username
		# session['firstname'] = dbData['firstname']
		# session['lastname'] = dbData['lastname']


		return jsonify("Successfully logged in as " + session['username']), 203



@app.route('/logout', methods=['GET'])
def logoutApi():
	session.pop('username', None)

	return redirect(url_for("api.loginApi"))


@app.route('/create-account', methods=['POST', 'GET'])
def createApi():
	if request.method == "GET":
		return render_template("createAccount.html")
	else:
		vals = request.get_json()
		# print(vals['username'])

		username = vals['username']
		firstname = vals['firstname']
		lastname = vals['lastname']
		password = vals['password']

		cur = db.cursor()

		# I need to add a hashing algorithm to secure the passwords in the databases 

		query = "SELECT username FROM accounts WHERE username=\"" + username + "\""
		cur.execute(query)
		dbData = cur.fetchone()

		if (dbData != None):
			return jsonify("This username already in use, please try something else"), 403

		query = "SELECT password FROM accounts WHERE password=\"" + password + "\""
		cur.execute(query)
		dbData = cur.fetchone()

		if (dbData != None):
			return jsonify("This password is already in use, please try something else"), 403

		query = "INSERT INTO accounts (username, password, firstname, lastname) VALUES (\"" + username + "\", \"" + password + "\", \"" + firstname + "\", \"" + lastname + "\")"   
		cur.execute(query)

		confirm = "created account for " + vals['firstname'] + " " + vals['lastname']
		return jsonify(confirm), 203