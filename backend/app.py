from flask import Flask
from kobo_functions import Kobo

app = Flask(__name__)

@app.route("/")
def main_app():
    return "<p>Main Page!</p>"

@app.route("/all")
def allbook():
    all_books=Kobo().shelf
    return all_books