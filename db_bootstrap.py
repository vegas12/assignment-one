import sqlite3

conn = sqlite3.connect('movies_database')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS movies
          ([movie_id] INTEGER PRIMARY KEY AUTOINCREMENT, [movie_name] TEXT)
          ''')

conn.commit()