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
    gender = db.Column(db.String(20), nullable=False)


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


"""
TEST SQL INPUT -
    
1. Four dummy CCAs
    INSERT INTO cca VALUES ('CCA 1');
    INSERT INTO cca VALUES ('CCA 2');
    INSERT INTO cca VALUES ('CCA 3');
    INSERT INTO cca VALUES ('CCA 4');

2. Five Users
    INSERT INTO baseuser (matric, password, name, gender) VALUES ('a1', '123123','Bob', 'm');
    INSERT INTO baseuser (matric, password, name, gender) VALUES ('a2', '123123','Alice', 'f');
    INSERT INTO baseuser (matric, password, name, gender) VALUES ('a3', '123123','Charlie', 'm');
    INSERT INTO baseuser (matric, password, name, gender) VALUES ('a4', '123123','Dickson', 'm');
    INSERT INTO baseuser (matric, password, name, gender) VALUES ('a5', '123123','Eusoff', 'f');

3. Relationship
    INSERT INTO ccamap VALUES ('a1','CCA 1', 10);
    INSERT INTO ccamap VALUES ('a1','CCA 3', 10);
    INSERT INTO ccamap VALUES ('a2','CCA 2', 10);
    INSERT INTO ccamap VALUES ('a3','CCA 4', 10);
    INSERT INTO ccamap VALUES ('a4','CCA 1', 10);
    INSERT INTO ccamap VALUES ('a4','CCA 2', 10);
    INSERT INTO ccamap VALUES ('a5','CCA 3', 10);
    INSERT INTO ccamap VALUES ('a5','CCA 1', 10);
"""
