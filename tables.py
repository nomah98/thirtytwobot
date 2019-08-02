from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey


class Roommate(db.Model):
    __tablename__ = 'roommates'
    name = db.Column(db.String(), primary_key=True)


class Insult(db.Model):
    __tablename__ = 'insults'
    name = db.Column(db.String(), ForeignKey('roommates.name'))
    insult = db.Column(db.String(), primary_key=True)
