from flask import Flask, render_template #called on the Jinja template, 
#Flask will return it to the browser 

app = Flask(__name__) #new instance of Flask class assigned to app variable

@app.route("/")
def index():
    """Show homepage"""

    return render_template("index.html") 
    #function renders this template, 
    #returns this route as html to the browser
    #Flask is exposing this route to the internet




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')