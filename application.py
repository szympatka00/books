import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register")
def register():
    return "Register"

@app.route("/login")
def login():
    return "Login"

@app.route("/logout")
def logout():
    return "Logout"

@app.route("/dashboard")
def dashboard():
    return "Dashboard"

@app.route("/book")
def book():
    return "book"
# page where they can search for a book. Users should be able to type in the ISBN number of a book,
#the title of a book, or the author of a book. After performing the search, your website should display
#a list of possible matching results, or some sort of message if there were no matches. If the user typed
#in only part of a title, ISBN, or author name, your search page should find matches for those as well!

if __name__ == '__main__':
    main()
