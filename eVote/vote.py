from sqlalchemy import Table, MetaData, Column, Boolean, String
from sqlalchemy.orm import mapper
import sqlalchemy


def gendeclarative(tablename, meta=MetaData()): 
	""" Manually map vote object and return it """
	t = Table(tablename, meta, 
			Column('username', String, primary_key=True), 
			Column('falias', String), 
			Column('lalias', String), 
			Column('vote', Boolean))
	m = mapper(Vote, t)
	return t, m

class Vote(object): 
	""" Vote Object, mapped to database """ 
	def __init__(self, username='none', falias='anonymous',
			lalias='anonymous', vote='W', table='vote'): 
		self.username = username
		self.falias = falias
		self.lalias = lalias
		self.vote = vote
		self.__tablename__ = table
		(t, m) = gendeclarative(table)
		self.__mapper__ = m
		self.__table__ = t
	def __repr__(self): 
		return "<eVote('%s', '%s', '%s', '%s')>" %\
			(self.username, self.falias, self.lalias, self.vote)
