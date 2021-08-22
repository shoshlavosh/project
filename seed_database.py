"""Seeds the database"""

import os #imports Python module from standard library
import json #need this to load the data in .json files
from datetime import datetime 
from random import choice, randint #for testing

import crud
import model
import server

#drop and recreate the database
os.system('dropdb tenants')
os.system('createdb tenants')

#connect to the database & call db.create_all()
model.connect_to_db(server.app) #connect to the db through model.py
model.db.create_all() #create db using model.py

#Note: datetime in the violations.json and complaints.json file is
#in this format: '%Y-%m-%dT%H:%M:%S.%f'
#variable = datetime.strptime(date_str, date_format)
#strptime means "string parse time"

# #create fake buildings to add to the database
for n in range(10):
    street_number = f'{n}'
    street_name = f'street{n}'
    street_suffix = f'Av'
    zip_code = f'94110'
    lat_long = f'{n}'

    #create building
    building = crud.create_building(street_number, street_name, 
    street_suffix, zip_code, lat_long)

#open up json files and parse through them, item by item
#add complaints to database

# with open('data/evictions.json') as f: #syntax is from the movie ratings lab
complaints_data = json.loads(open('data/complaints.json').read())

complaints_in_db = []

for complaint in complaints_data:
    complaint_number, complaint_description = (
        complaint['complaint_number'],
        complaint.get('complaint_description') #returns None if there
        #isn't a complaint_description
    )
    building_id = '1' #added for testing reasons
    # building_id = complaint['building_id']
    date_filed = datetime.strptime(complaint['date_filed'], '%Y-%m-%dT%H:%M:%S.%f')

    db_complaint = crud.create_complaint(complaint_number, building_id,
                                        complaint_description,
                                        date_filed) 
                                        #will need to add building_id

    complaints_in_db.append(db_complaint)

violations_data = json.loads(open('data/violations.json').read())

#add violations to the database
violations_in_db = []

for violation in violations_data:
    if not crud.get_complaint(violation['complaint_number']):
        crud.create_complaint(violation['complaint_number'], None, None, None)
    complaint_number, nov_category_description = (
        violation['complaint_number'],
        violation['nov_category_description']
    )
    item = None
    if 'item' in violation:
        item = violation['item']
    nov_item_description = None
    if 'nov_item_description' in violation:
        nov_item_description = violation['nov_item_description']
    building_id = '1' #added for testing purposes
    # building_id = violation['building_id']
    date_filed = datetime.strptime(violation['date_filed'], '%Y-%m-%dT%H:%M:%S.%f')

    db_violation = crud.create_violation(complaint_number, building_id, 
                                        nov_category_description,
                                        item, nov_item_description, 
                                        date_filed)

    violations_in_db.append(db_violation)

#create fake users & fake reviews to add to database
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)


    #create reviews for user
    for i in range(10):
        review__id = f'Test {i} review' #the above fake users didn't need this
        building_id = f'Building{i}' 
        user_id = f'User{i}'
        review_date = f'200{i}, 4, 3'
        review_text = 'test'
        rating = f'Rating {i}'
        landlord_name = f'Landlord{i}'


        crud.create_review(building_id, user_id, review_date, review_text, rating, landlord_name)
        # review = crud.create_review(review_id = '1', building_id='1', user_id='1', review_date='2002, 4, 3', review_text='test', rating=None, landlord_name=None)
        #also how do I code it in model.py so that the review_date is set automatically?
