from app import app
from server import Vendor, db

if __name__ == '__main__':
    with app.app_context():
        whole = Vendor(id=2, name="Whole Foods")
        db.session.add(whole)
        db.session.commit()
        