"""Seeds the database"""

import os
import json
from datetime import datetime

import crud
import model
import server

#open up json file and parse through it, item by item
#figure out how to connect it to model.py

# with open('data/evictions.json') as f: #this syntax is from the lab
complaints_data = json.loads(open('data/complaints.json').read())

print(complaints_data)

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
    