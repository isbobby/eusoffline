from eusoffline import create_app, db
from eusoffline.models import CCA, CCAMap, TopResidents
from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles

app = create_app()


@compiles(DropTable, "postgresql")
def _compile_drop_table(element, compiler, **kwargs):
    return compiler.visit_drop_table(element) + " CASCADE"


with app.app_context():
    # BaseUser.__table__.drop(db.engine)
    CCAMap.__table__.drop(db.engine)
    CCA.__table__.drop(db.engine)
    TopResidents.__table__.drop(db.engine)
    db.create_all()
