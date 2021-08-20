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

#open up json files and parse through them, item by item

# with open('data/evictions.json') as f: #syntax is from the movie ratings lab
complaints_data = json.loads(open('data/complaints.json').read())

complaints_in_db = []

for complaint in complaints_data:
    complaint_number, complaint_description = (
        complaint['complaint_number'],
        complaint['complaint_description']
    )
    building_id = '1' #added for testing reasons
    date_filed = datetime.strptime(complaint['date_filed'], '%Y-%m-%dT%H:%M:%S.%f')

    db_complaint = crud.create_complaint(complaint_number, building_id,
                                        complaint_description,
                                        date_filed) 
                                        #will need to add building_id

    complaints_in_db.append(db_complaint)

violations_data = json.loads(open('data/violations.json').read())

#print(violations_data)

#datetime in the violations.json and complaints.json file is
#in this format: '%Y-%m-%dT%H:%M:%S.%f'
#variable = datetime.strptime(date_str, date_format)
#strptime means "string parse time"

#Create complaints, store them in a list to create fake complaints later
complaints_in_db = []

# for complaints in complaints_data:










#From movie ratings app:

# import os
# import json
# from random import choice, randint
# from datetime import datetime

# import crud
# import model
# import server

# os.system('dropdb ratings')
# os.system('createdb ratings')

# model.connect_to_db(server.app)
# model.db.create_all()

# with open('data/movies.json') as f:
#     movie_data = json.loads(f.read())

# #Create movies, store them in list so we can use them
# #to create fake ratings later
# movies_in_db = []
# for movie in movie_data:
    
#     #TODO: get the title, overview, and poster_path from the movie
#     #dictionary. Then, get the release_date and convert it to a 
#     #datetime object with datetime.strptime
    