import sqlite3

class Kobo: 
    def __init__(self):
        self.shelf=self.fetch_all_books()

    def fetch_all_books(self):
        # Connect to database (or create one)
        connection = sqlite3.connect('/Users/cuilide/Desktop/book_tools/KoboReader.sqlite')

        # Create a cursor
        cursor = connection.cursor()

        # Query
        cursor.execute('''
            SELECT * FROM 'content' WHERE ContentType=6
        ''')
        rows = cursor.fetchall()

        connection.close()
        return rows
