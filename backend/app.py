from flask import Flask
from kobo_functions import Kobo

app = Flask(__name__)

@app.route("/")
def main_app():
    return "<p>Main Page!</p>"

#TODO need to clean up
@app.route("/all")
def allbook():
    print('All books')
    all_books=Kobo().shelf
    print(all_books)
    return all_books