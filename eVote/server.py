from flask import Flask, json, request
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Float, String, Boolean
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO); 

engine = sqlalchemy.create_engine('mysql+pymysql://evote:evote@localhost:3306/eVote')
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

app.debug = True

@app.route('/')
def hello_world(): 
	return "eVote!"

@app.route('/polls', methods = ['POST'])
def api_message(): 
	return ""

if __name__ == "__main__": 
	print "SQLAlchemy v"+sqlalchemy.__version__
	app.run();
