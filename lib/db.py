import sqlite3
import os
from datetime import datetime


class DBA:
    __doc__ = """Database api for storing messages to improve Jake's future responses."""

    def __init__(self, path="Jake.db",**kwargs):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_table(self,table,**kwargs):
        """Creates a table with table_name as parameter table"""

        sql = "CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, Text TEXT, Date TEXT, Time TEXT)"
        try:
            self.cursor.execute(sql.format(table))
        except Exception as e:
            print(e)
            return False
        else:
            print("Table(s) {} created".format(table))
            return True

    def create_error(self, msg, date=str(datetime.now().date()), time=str(datetime.now().time())):
        """Used to enter messages into the database"""

        try:
            self.cursor.execute("INSERT OR IGNORE INTO ErrorMsgs (Text,Date,Time) VALUES(?,?,?)",(msg, date, time))
        except Exception as e:
            print (e)
            return False
        else:
            print("Message saved")
            self.conn.commit()
            # self.query_errors()
            return True

    def query_errors(self, **kwargs):
        """Queries the database, receives arguments(table columns) if any to build an sql statement
        for fetching queries, if no parameter is given, it will output everything in the database"""
        count=0
        if kwargs:
            sql = "SELECT * FROM ErrorMsgs"
            for index,(key,value) in enumerate(kwargs.items(),1):
                if index < 2:
                    sql += " WHERE {} = '{}'".format(key,value)
                else:
                    sql += " AND {} = '{}'".format(key, value)
        else:
            sql = "SELECT * FROM ErrorMsgs"
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            return False
        else:
            print(self.cursor.fetchall())
            return True

    def update_error(self, text_id, new_text ,date=str(datetime.now().date()), time=str(datetime.now().time())):
        """Used to update a row in the table"""
        try:
            self.cursor.execute("UPDATE TABLE ErrorMsgs SET Text={}, Date={},Time={} WHERE id={}".format(new_text,date,time,text_id))
        except Exception as e:
            print(e)
            return False
        else:
            print("Updated")
            return True

    def delete_error(self, id):
        """Used to delete a row"""
        try:
            self.cursor.execute("DELETE FROM TABLE ErrorMsgs WHERE id={}".format(id))
        except Exception as e:
            print(e)
            return False
        else:
            print("Deleted")
            return True
