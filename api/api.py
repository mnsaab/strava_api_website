from flask import *
from extensions import db
import os
import re
import hashlib
import uuid

api = Blueprint('api', __name__, template_folder='templates')

@api.route('/home', methods=['POST', 'GET'])
def homeApi():
	print("hello")