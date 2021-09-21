"""Seeds the database"""

import os #imports Python module from standard library
import json #need this to load the data in .json files
from datetime import datetime 
from random import choice, randint #for testing

import crud
import model
from model import Building
import server


#drop and recreate the database
os.system('dropdb tenants')
os.system('createdb tenants')

#connect to the database & call db.create_all()
model.connect_to_db(server.app, echo=False) #connect to the db through model.py
#echo=False to cut down on terminal output so it's easier to see error messages
model.db.create_all() #create db using model.py

#Note: datetime in the violations.json and complaints.json file is
#in this format: '%Y-%m-%dT%H:%M:%S.%f'
#variable = datetime.strptime(date_str, date_format)
#strptime means "string parse time"

#open up json files and parse through them, item by item
#add complaints to database

complaints_data = json.loads(open('data/complaints.json').read())

complaints_in_db = []

for complaint in complaints_data:
    #if building doesn't exist in the buildings table already:
    building = Building.query.filter(Building.street_number==complaint['street_number'], Building.street_name==complaint['street_name'], Building.street_suffix==complaint['street_suffix'], Building.zip_code==complaint['zip_code']).first()
    if not building:
        #then create new building
        building = crud.create_building(complaint['street_number'], \
                            complaint['street_name'], complaint['street_suffix'], \
                            complaint['zip_code'])

    complaint_number, complaint_description = (
        complaint['complaint_number'],
        complaint.get('complaint_description') #returns None if there
        #isn't a complaint_description
    )
    date_filed = datetime.strptime(complaint['date_filed'], '%Y-%m-%dT%H:%M:%S.%f')

    db_complaint = crud.create_complaint(complaint_number, building.building_id,
                                        complaint_description,
                                        date_filed) 
                                       

    complaints_in_db.append(db_complaint)

violations_data = json.loads(open('data/violations.json').read())

#add violations to the database
violations_in_db = []

for violation in violations_data:
    building = Building.query.filter(Building.street_number==violation['street_number'], Building.street_name==violation['street_name'], Building.street_suffix==violation.get('street_suffix', None), Building.zip_code==violation.get('zip_code', None)).first()
    if not building:
        #then create new building
        building = crud.create_building(violation['street_number'], \
                            violation['street_name'], violation.get('street_suffix', None), \
                            violation.get('zip_code', None))
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

    date_filed = datetime.strptime(violation['date_filed'], '%Y-%m-%dT%H:%M:%S.%f')

    db_violation = crud.create_violation(complaint_number, building.building_id, 
                                        nov_category_description,
                                        item, nov_item_description, 
                                        date_filed)

    violations_in_db.append(db_violation)

#create fake users to add to database
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)