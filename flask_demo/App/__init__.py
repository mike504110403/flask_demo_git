from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# connect between flask & SQL
app = Flask(__name__)
app.config.from_object('config')  # use config.py(info of SQL)
db = SQLAlchemy(app)  # connect to databases
