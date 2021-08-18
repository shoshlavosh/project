"""CRUD operations"""

from model import db, User, Building, Complaint, Violation, Review, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_building(address, street_number, street_name, street_suffix, zip_code, lat_long):
    """Create and return a building"""

    building = Building(address=address, street_number=street_number, street_name=street_name, street_suffix=street_suffix, zip_code=zip_code, lat_long=lat_long)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)