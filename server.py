from flask import (Flask, render_template, request, flash, session, redirect)
#render_template is called on the Jinja template, 
#Flask will return it to the browser 

from model import connect_to_db
import crud

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



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')