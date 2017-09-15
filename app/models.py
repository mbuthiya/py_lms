from . import db

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer,primary_key = True)
    day_number = db.Column(db.Integer)
    week_number = db.Column(db.Integer)
    body = db.Column(db.String)
    lessons = db.Column(db.String)
