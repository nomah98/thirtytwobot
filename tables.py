from app import db
from sqlalchemy.orm import scoped_session,sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy import Table, Column, Integer, ForeignKey

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class Roommate(db.Model):
    __tablename__ = 'roommates'
    name = db.Column(db.String(), primary_key=True)


class Insult(db.Model):
    __tablename__ = 'insults'
    name = db.Column(db.String(), ForeignKey('roommates.name'))
    phrase = db.Column(db.String(), primary_key=True)
