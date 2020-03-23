from eusoffline import db, create_app
from eusoffline.models import BaseUser
import pandas as pd

userCSV = pd.read_csv("./ResidentPassword.csv")

app = create_app()

with app.app_context():
    for index, row in userCSV.iterrows():
        # matric, name, password
        new_user_entry = BaseUser(
            matric=row[3].upper(), name=row[4], password=row[5])
        db.session.add(new_user_entry)
    db.session.commit()
