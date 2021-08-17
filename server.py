from Flask import render_template #called on the Jinja template, 
#Flask will return it to the browser 

app = Flask(__name__) #new instance of Flask class assigned to app variable

@app.route("/")
def root():
    """Root route"""

    return render_template("root.html") 
    #function renders this template, 
    #returns this route as html to the browser
    #Flask is exposing this route to the internet