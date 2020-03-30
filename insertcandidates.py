from eusoffline import db, create_app
from eusoffline.models import Candidates

app = create_app()

with app.app_context():
    new_candidate_entry1 = Candidates(
        name="Brenda Ho", category="presidential", description="Y2 Business Administration")
    new_candidate_entry2 = Candidates(
        name="Hoo Jinh Hao", category="presidential", description="Y3 Engineering Science")
    new_candidate_entry3 = Candidates(
        name="Amos Cheah", category="presidential", description="Y3 Applied Mathematics")
    db.session.add(new_candidate_entry1)
    db.session.add(new_candidate_entry2)
    db.session.add(new_candidate_entry3)
    db.session.commit()
