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
    id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(50), db.ForeignKey('baseuser.matric'))
    cca = db.Column(db.String(255), db.ForeignKey('cca.name'))
    points = db.Column(db.Integer)


"""
TEST SQL INPUT -

INIT -
    DROP TABLE baseuser CASCADE;
    DROP TABLE cca CASCADE;
    DROP TABLE ccamap CASCADE;
    
1. Four dummy CCAs
    INSERT INTO cca VALUES ('CCA 1');
    INSERT INTO cca VALUES ('CCA 2');
    INSERT INTO cca VALUES ('CCA 3');
    INSERT INTO cca VALUES ('CCA 4');

2. Five Users
    INSERT INTO baseuser VALUES (1, 'A1', '123123','Bob');
    INSERT INTO baseuser VALUES (2, 'A2', '123123','Alice');
    INSERT INTO baseuser VALUES (3, 'A3', '123123','Charlie');
    INSERT INTO baseuser VALUES (4, 'A4', '123123','Dickson');
    INSERT INTO baseuser VALUES (5, 'A5', '123123','Eusoff');

3. Relationship
    INSERT INTO ccamap VALUES (1,'A1','CCA 1', 10);
    INSERT INTO ccamap VALUES (2,'A1','CCA 3', 10);
    INSERT INTO ccamap VALUES (3,'A2','CCA 2', 10);
    INSERT INTO ccamap VALUES (4,'A3','CCA 4', 10);
    INSERT INTO ccamap VALUES (5,'A4','CCA 1', 10);
    INSERT INTO ccamap VALUES (6,'A4','CCA 2', 10);
    INSERT INTO ccamap VALUES (7,'A5','CCA 3', 10);
    INSERT INTO ccamap VALUES (8,'A5','CCA 1', 10);
"""
