from eusoffline import db, create_app
from eusoffline.models import TopResidents
import pandas as pd

userCSV = pd.read_csv("./topresidents.csv")

app = create_app()

with app.app_context():
    for index, row in userCSV.iterrows():
        new_user_entry = TopResidents(name=row[0])
        db.session.add(new_user_entry)
    db.session.commit()
