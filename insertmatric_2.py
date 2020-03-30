from eusoffline import db, create_app
from eusoffline.models import BaseUser
import pandas as pd

userCSV = pd.read_csv("./newResidentPassword.csv")

app = create_app()

with app.app_context():
    for index, row in userCSV.iterrows():
        # index,name,matric,password
        # matric, name, password
        new_user_entry = BaseUser(
            matric=row[2].upper(), name=row[1], password=row[3])
        db.session.add(new_user_entry)
    db.session.commit()
