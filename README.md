# project_tenant_helper

Project Description:

Tech Stack:
* Python 
* JavaScript 
* HTML
* jQuery 
* Jinja
* Bootstrap 
* CSS
* Flask
* SQLAlchemy 
* PostgreSQL 
* AJAX
* APIs: San Francisco Department of Building Inspection, Google Maps, and Google Geocoding

Features:

Homepage:
Navigation Bar
Description of Tenant Helper App
Create an Account
Log In

Search Page:
Search for an Address
* Enter a street address to navigate to a building's page
* If there isn't already a building for an address in the database, a new one will be added

View a List of All Buildings by Address
* Click on any link to view that building's page

Building Page:
* Shows an interactive Google Map with a marker centered on the address
* Lists any complaints, violations, and reviews for that building
* Includes an area for users to add a review for that building


Instructions / How to Install:

Set up and activate a virtual environment:
>>>virtualenv env
>>>source env/bin/activate

Install frameworks & libraries:
>>>pip3 install -r requirements.txt

Seed the database:
>>>python3 seed_database.py

Run the server:
>>>python3 server.py
(then, open in browser)
