import sqlite3
table  = ["odessa",555]
db = sqlite3.connect('sql\sql.db')
cursor = db.cursor()
cursor.execute('UPDATE user SET city ==? WHERE id ==?',table)
db.commit()
db.close()

