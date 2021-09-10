from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
#render_template is called on the Jinja template, 
#Flask will return it to the browser 

from model import connect_to_db
import crud

from datetime import datetime

from jinja2 import StrictUndefined #shows errors if there's an undefined variable

app = Flask(__name__) #new instance of Flask class assigned to app variable
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Show homepage"""

    return render_template("index.html") 
    #function renders this template, 
    #returns this route as html to the browser
    #Flask is exposing this route to the internet

@app.route("/buildings")
def view_buildings():
    """Show all buildings"""

    buildings = crud.get_buildings()

    return render_template("all_buildings.html", buildings=buildings)


@app.route("/buildings/<building_id>")
def show_building(building_id):
    """Show details of a particular building"""

    building = crud.get_building_by_id(building_id)

    # print("*"*20)
    # print(building.reviews[0].review_date.strftime('%Y-%m-%d'))
    # print("*"*20)

    return render_template("building_details.html", building=building,
                            complaints=building.complaints, 
                            violations=building.violations,
                            reviews=building.reviews) 


@app.route("/users")
def view_users():
    """Show all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details of a particular user"""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/users", methods=['POST'])
def register_user():
    """Create a new user."""
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    #check to see if user already exists
    if user:
        flash("A user with this email already exists. Please try again.")

    else:
        #create new user
        crud.create_user(email, password)
        flash("Your account was created successfully! You can now log in.")
        
    return redirect("/")


@app.route("/login", methods=['POST'])
def handle_login():
    """Log user in"""

    email = request.form['email'] 
    password = request.form['password']
    #note: lab exercise solution used request.form.get()

    user = crud.get_user_by_email(email)

    if not user:
        flash("Error: This user does not exist.")
        flash("Please create an account below.")
        return redirect("/")

    if user.password != password:
        flash("Error: wrong password.")
        return redirect("/") #redirects to homepage
    
    else:
        session['user_email'] = user.email #adds key to Flask session
        flash(f'Logged in. Welcome back, {user.email}!')
        #maybe change this to return a menu template where user can 
        #choose to search for an address, create a review, etc.
        # return render_template("/address_search.html") 
        return redirect("/search")


@app.route("/search")
def search():
    """Route user to the search page"""

    return render_template("address_search.html")


@app.route("/address_search", methods=['POST']) 
def handle_address():
    """Handle address entered by a user"""

    street_number = request.form['street_number']
    street_name = request.form['street_name']
    street_suffix = request.form['street_suffix']
    zip_code = request.form['zip_code']

    building = crud.get_building_by_address(street_number, street_name, 
                                            street_suffix, zip_code)
                                        
    if not building:
        building = crud.create_building(street_number, street_name, 
                            street_suffix, zip_code)
        flash(f'New building created: Building ID #{building.building_id}')

    return redirect(f"/buildings/{building.building_id}") #redirects to 
                                                        #building's page


@app.route("/review/<building_id>", methods=["GET", "POST"])
def create_review(building_id):
    """Add a review to a building's page"""

 
    building = crud.get_building_by_id(building_id)

    user = crud.get_user_by_email(session.get("user_email"))

    if request.method == 'POST':
        if not user:
            flash("Error: Please log in to leave a review.")
            return redirect("/") #redirects to homepage
    
        review_text = request.form['review_text']

        landlord_name = request.form['landlord_name']

        # if not review_text:
        #     flash("Error: Please enter review text")
        #     return redirect("/review/<building_id>")

        review = crud.create_review(building_id=building_id, 
                                user_id=user.user_id,
                                review_date=datetime.now().strftime('%Y-%m-%d'), #format?
                                review_text=review_text,
                                landlord_name=landlord_name)
        return render_template("review_text.html", review=review) #for a POST request

    return render_template("building_details.html", building=building) #for a GET request



@app.route("/map")
def show_map():
    """Show Google Map"""

    return render_template("map.html")


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')