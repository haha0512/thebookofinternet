import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'''mysql+pymysql://{os.environ['db_id']}:{os.environ['db_pass']}@thebookofinternet-db-instance.cx9rgbotmuld.ap-northeast-2.rds.amazonaws.com:3306/development'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
limiter = Limiter(app, key_func=get_remote_address)

import thebookofinternet.views