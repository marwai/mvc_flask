# import flask
from flask import Flask, render_template, url_for, request
from markupsafe import escape
# In order for us to use flask we need to crate an instance of our app
app = Flask(__name__) # __ is syntax to create flask


# Syntax to create flask instance

# Syntax for decorators to create a web route
# block of code for default page
@app.route("/")

# Create a welcome method to display on home page
def index():
    return "<h1>Welcome to MVC with flask project</h1>"
# eng of block of code for default page

# index method will be called at the endpoint
# index method will display on our home page
if __name__ == "__main__": # syntax to run app
    app.run(debug=True)
    # debug = true to ensure upate any changes without re-running the app

# When you seen an error/exception - look at the line number at the end of error and review your code first

# exercise: - create a function called welcome_user
# create a decorator to link the page/user
# return "Welcome to Python flask app dear {user}"
# @app.route("/<username>")
# def welcome_user(username):
#     return f"<h1> Welcome to Python flask app dear {username} </h1>"

@app.route("/")
def main_page():
    return render_template("base.html")


@app.route("/login/")
def welcome_user():
    # login in functionality with GET, POST methods of HTTP
    # import request to use the methods check status code
    # add control flow to redirect the user according to the status code received
    return render_template("index.html")


