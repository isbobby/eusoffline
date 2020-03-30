from eusoffline import db
from flask_user import UserMixin


class BaseUser(db.Model, UserMixin):
    __tablename__ = 'baseuser'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    # User authentication information
    matric = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255))


class CCA(db.Model):
    __tablename__ = 'cca'
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(255), primary_key=True)


class CCAMap(db.Model):
    __tablename__ = 'ccamap'
    __table_args__ = {'extend_existing': True}
    # id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(50), db.ForeignKey(
        'baseuser.matric'), primary_key=True)
    cca = db.Column(db.String(255), primary_key=True)
    role = db.Column(db.String(255), primary_key=True)
    points = db.Column(db.Integer, primary_key=True)


class TopResidents(db.Model):
    __tablename__ = 'topresidents'
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(255), primary_key=True)


class Candidates(db.Model):
    __tablename__ = 'candidates'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    description = db.Column(db.String(255))


class Votes(db.Model):
    __tablename__ = 'votes'
    __table_args__ = {'extend_existing': True}
    voter = db.Column(db.String(50), db.ForeignKey(
        'baseuser.matric'), primary_key=True)
    target_id = db.Column(db.Integer, db.ForeignKey(
        'candidates.id'), primary_key=True)
    vote = db.Column(db.Integer)
