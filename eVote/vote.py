from sqlalchemy import Table, MetaData, Column, Boolean, String
from sqlalchemy.orm import mapper
import sqlalchemy


def votemap(tablename, meta=MetaData()): 
	""" Manually map vote object and return it """
	vote = Table(tablename, meta, 
			Column('username', String, primary_key=True), 
			Column('falias', String), 
			Column('lalias', String), 
			Column('vote', Boolean))
	mapper(Vote, vote)
	return vote

class Vote(object): 
	""" Vote Object, mapped to database """ 
	def __init__(self, username, falias, lalias, vote): 
		self.username = username
		self.falias = falias
		self.lalias = lalias
		self.vote = vote

