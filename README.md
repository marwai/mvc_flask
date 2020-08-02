# MVC Module View Controller 

In python we are using the Flask micro-framework to develop a web application that follows the MVC development
pattern.

![MVC](images/MVC_Diagram.png)

| Model                                                                                            	| View                                                                                                   	| Controller                                                                                                                                                       	|
|--------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Includes all data and its related logic (a way for talking about data) 	|   Presents data and its related logic (a way for talking about user interfaces) MVC is HTML, CSS and some special syntax. 	| An interface between Model and View components (a way for talking about program logic) aka the request handler 

Benefits of MVC
* Using Python flask to interacts with users on the web

Basic code structure:

```html
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

```

Setting up flask
```bash
import flask
from flask import Flask
```
In order for us to use flask we need to crate an instance of our app.
```bash 
app = Flask(__name__) # __ is syntax to create flask
```

Syntax to create flask instance.
Syntax for decorators to create a web route
block of code for default page, so decorator is declared. 
```bash
 @app.route("/") ```

Create a welcome method to display on home page
```bash
 def index():
    return "<h1>Welcome to MVC with flask project</h1>" 
```
End of block of code for default page.

index method will be called at the endpoint
index method will display on our home page
``` if __name__ == "__main__": # syntax to run app
    app.run(debug=True)
    # debug = true to ensure upate any changes without re-running the app
```

exercise: - create a function called welcome_user
create a decorator to link the page/user
return "Welcome to Python flask app dear {user}"
```
@app.route("/<username>")
def welcome_user_profile(username):
    return f"<h1> Welcome to Python flask app dear {username} </h1>"
```