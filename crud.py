"""CRUD operations"""

from model import db, User, Building, Complaint, Violation, Review, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_building(address, street_number, street_name, street_suffix, zip_code, lat_long):
    """Create and return a new building"""

    building = Building(address=address, street_number=street_number, 
    street_name=street_name, street_suffix=street_suffix, zip_code=zip_code, 
    lat_long=lat_long)

    db.session.add(building)
    db.session.commit()

    return building


def create_complaint(complaint_number, building_id, description, date_filed):
    """Create and return a new complaint"""

    complaint = Complaint(complaint_number=complaint_number, 
                        building_id=building_id, description=description, 
                        date_filed=date_filed)

    db.session.add(complaint)
    db.session.commit()

    return complaint


def create_violation(complaint_number, building_id, description, date_filed):
    """Create and return a new violation"""

    violation = Violation(complaint_number=complaint_number, 
                        building_id=building_id, description=description, 
                        date_filed=date_filed)

    db.session.add(violation)
    db.session.commit()


# def create_review(review_id, building_id, user_id, review_date, review_text, rating, landlord_name):
#     """Create and return a new review."""

#     review = Review(review_id=review_id, building_id=building_id, 
#                     user_id=user_id, review_date=review_date, 
#                     review_text=review_text, rating=rating, 
#                     landlord_name=landlord_name)

#     db.session.add(review)
#     db.session.commmit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)