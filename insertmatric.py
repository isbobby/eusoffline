from eusoffline import db, create_app
from eusoffline.models import BaseUser

import pandas as pd
userCSV = pd.read_csv("./allmatric.csv")

app = create_app()

with app.app_context():
    for index, row in userCSV.iterrows():
        # matric, name, gender
        new_user_entry = BaseUser(matric=row[0].upper(), name=row[1], gender=row[2])
        db.session.add(new_user_entry)
    db.session.commit()
