from eusoffline import db, create_app
from eusoffline.models import CCAMap

import math
import pandas as pd
CCACSV = pd.read_csv("./ccamap.csv")

app = create_app()

with app.app_context():
    for index, row in CCACSV.iterrows():
        # matric, cca, role, points
        matric = str(row[0]).upper()
        cca = "Not Available"
        role = "Not Available"
        points = 0

        if (math.isnan(row[3])):
            points = 0
        else:
            points = row[3]

        role = row[2]
        cca = row[1]

        new_cca_entry = CCAMap(matric=matric, cca=cca, role=role, points=points)
        db.session.add(new_cca_entry)
    db.session.commit()
