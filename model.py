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


    def __repr__(self):
        """Show info about user"""
        return f'<User user_id={self.user_id} email={self.email}'

    
class Building(db.Model):
    """A building"""

    __tablename__ = 'buildings'

    building_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    address = db.Column(db.String)
                        # unique=True? 
                        #there are addresses listed in the dataset
                        #for complaints, but I also want users to be able
                        #to enter an address when they make a review

    def __repr__(self):
        """Show info about a building"""
        return f'<Building building_id={self.building_id} address={self.address}>'
    

class Complaint(db.Model):
    """A building code complaint"""

    __tablename__ = 'complaints'

    complaint_id = db.Column(db.Integer, #this is listed in the data set
                            primary_key=True)
    building_id = db.Column(db.Integer, 
                            db.ForeignKey('buildings.building_id'))
    address = db.Column(db.String) #should this be connected as a FK from
                                    #buildings? I'm sourcing it from the 
                                    #complaints data set
    description = db.Column(db.String)
    date_filed = db.Column(db.DateTime) #or should I do this as an int 
                                        #since it's coming from the dataset

    def __repr__(self):
        """Show a complaint"""
        return f'<Complaint complaint_id={self.complaint_id} building_id={self.building_id} description={self.description}>'


class Review(db.Model):
    """A review of a building / landlord"""

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

    def __repr__(self):
        """Show a review"""
        return f'<Review review_id={self.review_id} building_id={self.building_id} review_text={self.review_text}>'


if __name__ == 'main':
    from server import app

    connect_to_db(app)
