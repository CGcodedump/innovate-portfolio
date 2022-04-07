########################################
#? FLASK APPLICATION
########################################

# Extensions that allow specific classes and functions
from flask import Flask, render_template, url_for, redirect

# The website is defined as a flask app and the url prefix is set to '/'
app = Flask(__name__)

########################################
#? PAGES
########################################

# This is how the homepage is accessed
@app.route("/")
def home ():
    return render_template("index.html")

@app.route("/fcleaders")
def fc_leaders():
    return render_template("fcleaders.html")

@app.route("/gallery")
def fc_gallery():
    return render_template("gallery.html")

@app.route("/estate")
def fc_estate():
    return render_template("estate.html")

@app.route("/contactus")
def contact_us():
    return render_template("contactus.html") 
#page_name = "Connor's Things", favourite_thing = "Final Fantasy XIV"

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

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

########################################

# Debugging is activated and the project is set to be hosted on port 8000. (Debugging should be only be used in testing)
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

########################################