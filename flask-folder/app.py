########################################
#? FLASK APPLICATION
########################################

# Extensions that allow specific classes and functions
from flask import Flask, Blueprint, render_template, url_for, redirect

# A 'Blueprint' of the website structure.
views = Blueprint(__name__, "views")

# The website is defined as a flask app and the url prefix is set to '/'
app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

########################################
#? PAGES
########################################

# This is how the homepage is accessed
@app.route("/")
def home ():
    return render_template("index.html")

@app.route("/connor")
def connor_page():
    return render_template("connor.html", page_name = "Connor", favourite_thing = "Pizza")

@app.route("/stuff")
def stuff_page():
    return render_template("stuff.html", page_name = "Connor's Stuff", favourite_thing = "Video Games")

@app.route("/things")
def things_page():
    return render_template("things.html", page_name = "Connor's Things", favourite_thing = "Final Fantasy XIV")

########################################
#? REDIRECT
########################################

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

########################################
#? ERRORS
########################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

########################################

# Debugging is activated and the project is set to be hosted on port 8000. (Debugging should be only be used in testing)
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

########################################