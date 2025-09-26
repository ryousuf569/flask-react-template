# Main configuration of our application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS #CROSS ORIGIN REQUESTS (Sends a request to this backend from a different URL)

# we want our frontend to connect with our backend, we do that using cors

app = Flask(__name__) # Initializes flask application
CORS(app) # Wrap our app in cors, disables the faulty URL error

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #location of the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # Creates a database instance which gives us access to the database defined above