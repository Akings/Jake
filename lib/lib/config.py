import sqlite3
from lib.db import *
""" Set up sql configurations here """
table_name = "Robot"
conn = sqlite3.connect('Robot.db')
cursor = conn.cursor()
try:
    cur = cursor.execute("SELECT * FROM {}".format(table_name))
except:
    columns = []
else:
    columns = [x[0] for x in cur.description]