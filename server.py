from flask import (Flask, render_template, request, flash, session, redirect)
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

    return render_template("building_details.html", building=building) 


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
    #note: solution used request.form.get()

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Error: wrong password.")
        return redirect("/") #redirects to homepage
    
    else:
        session['user_email'] = user.email #adds primary key to Flask session
        flash(f'Logged in. Welcome back, {user.email}!')
        return redirect("/") #redirect to review page


#how do I get this to pull info from user and building
#since user is logged in and on a building's page
@app.route("/review/<building_id>", methods=["POST"])
def create_review(building_id):
    """Add a review to a building's page"""

    building = crud.get_building_by_id(building_id)

    user = crud.get_user_by_email(session.get("user_email"))
    
    review_text = request.form['review_text']

    review = crud.create_review(building_id=building_id, 
                                user_id=user.user_id, #this works if I put in a default
                                review_date=datetime.now(), #format?
                                review_text=review_text)

    return render_template("building_details.html", building=building)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')