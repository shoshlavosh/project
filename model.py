"""Models for tenant helper app"""

#import the SQLAlchemy constructor function
from flask_sqlalchemy import SQLAlchemy

#calling the constructor function, creating an instance of 
#SQLAlchemy & assigning it to the variable "db"
db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    #relationship
    review = db.relationship("Review")

    def __repr__(self):
        """Show info about user"""
        return f'<User user_id={self.user_id} email={self.email}'

    
class Building(db.Model):
    """A building"""

    __tablename__ = 'buildings'

    building_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    address = db.Column(db.String) #create using fields below: street_number etc.
                        # unique=True? 

    street_number = db.Column(db.String) #it's str in the dataset, should I change it to int?
    street_name = db.Column(db.String)
    street_suffix = db.Column(db.String)
    zip_code = db.Column(db.String) #it's str in the dataset, should I change it to int?
    lat_long = db.Column(db.Integer)

    #relationships
    complaint = db.relationship("Complaint")
    violation = db.relationship("Violation")
    review = db.relationship("Review")


    def __repr__(self):
        """Show info about a building"""
        return f'<Building building_id={self.building_id} address={self.address}>'
    

class Complaint(db.Model):
    """A building code complaint"""

    __tablename__ = 'complaints'

    complaint_number = db.Column(db.Integer, 
                            primary_key=True)
    building_id = db.Column(db.Integer, 
                            db.ForeignKey('buildings.building_id'))
    description = db.Column(db.String)
    date_filed = db.Column(db.DateTime) #convert from str to 
                                        #datetime obj (see geeksforgeeks)
                                        #link from Jennifer

    building = db.relationship("Building") #relationship
    violation = db.relationship("Violation")

    def __repr__(self):
        """Show a complaint"""
        return f'<Complaint complaint_number={self.complaint_number} building_id={self.building_id} description={self.description}>'


class Violation(db.Model):
    """A building code violation"""

    __tablename__ = 'violations'

    complaint_number = db.Column(db.Integer, 
                            db.ForeignKey('complaints.complaint_number'),
                            primary_key=True)
    building_id = db.Column(db.Integer, 
                            db.ForeignKey('buildings.building_id'))
    description = db.Column(db.String)
    date_filed = db.Column(db.DateTime) #convert from str to 
                                        #datetime obj (see geeksforgeeks)
                                        #link from Jennifer

    building = db.relationship("Building") #relationships
    complaint = db.relationship("Complaint") 

    def __repr__(self):
        """Show a violation"""
        return f'<Violation complaint_number={self.complaint_number} building_id={self.building_id} description={self.description}>'


class Review(db.Model):
    """A review of a building / landlord"""

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    building_id = db.Column(db.Integer, 
                            db.ForeignKey('buildings.building_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    review_date = db.Column(db.DateTime)
    review_text = db.Column(db.String)
    rating = db.Column(db.Integer) #this is for 2nd sprint
    landlord_name = db.Column(db.String) 

    #relationships
    building = db.relationship("Building")
    user = db.relationship("User")

    def __repr__(self):
        """Show a review"""
        return f'<Review review_id={self.review_id} building_id={self.building_id} review_text={self.review_text}>'


def connect_to_db(flask_app, db_uri="postgresql:///tenants", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == 'main':
    from server import app

    connect_to_db(app)
