# project_tenant_helper

Project Description:

When you're looking for a place to live, it's hard to know what's going on "under the hood" of a particular apartment. Tenant Helper sources historical data about complaints and violations from the San Francisco Department of Building Inspection, and displays reviews from other tenants who've shared their experiences. Users can search for an address to view a building's data, leave a review, or read other user reviews. A building's page includes an interactive Google Map with a location marker centered on the address, and a list of complaints, violations, and reviews. Users can also create an account and log in.

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

FEATURES

Homepage:
* Navigation Bar
* Description of Tenant Helper App
* Create an Account
* Log In

Search Page:
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
>virtualenv env
>source env/bin/activate

Install frameworks & libraries:
>pip3 install -r requirements.txt

Seed the database:
>python3 seed_database.py

Run the server:
>python3 server.py
(then, open in browser)
