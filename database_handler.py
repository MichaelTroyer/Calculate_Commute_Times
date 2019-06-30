# -*- coding: utf-8 -*-
"""
Created on Sat June 29th 21:49 2019
@author: michael
"""


import os
import sqlite3


class Database():
    """
    Database is a class for handling database creation as well as adding and
    retrieving CommuteTime data.
    """

    def __init__(self, db_path):
        self.db_path = db_path
        if not os.path.exists(db_path):
            print('Creating database: {}'.format(db_path))
            self.build_database()

    def build_database(self):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()

            cur.execute("CREATE TABLE CommuteTimes("
                        "Datetime DATE,"
                        "Origin TEXT,"
                        "Destination TEXT,"
                        "Distance INTEGER,"
                        "Summary TEXT,"
                        "Fastest REAL,"
                        "Slowest REAL,"
                        "Warnings TEXT"
                        ");")

    def add_data(self, data):
        """
        Add data to database. Expects a dictionary.
        """
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO CommuteTimes values (?,?,?,?,?,?,?,?)",
                    (
                        data['Datetime'],
                        data['Origin'],
                        data['Destination'],
                        data['Distance'],
                        data['Summary'],
                        data['Fastest'],
                        data['Slowest'],
                        data['Warnings'],
                    )
                    )
        except Exception as e:
            print('Error writing data to database:', e)

    def get_data(self, start_date=None, end_date=None):
        """
        Return data from database between start_date and end_date.
        """
        #TODO: add source and destination filtering options
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                if start_date:
                    if end_date:
                        rows = cur.execute(
                            "SELECT * FROM CommuteTimes WHERE (Datetime > ? AND Datetime < ?)",
                            (start_date, end_date)
                            )
                    else:
                        rows = cur.execute(
                            "SELECT * FROM CommuteTimes WHERE Datetime > ?",
                            (start_date)
                            )
                else:
                    rows = cur.execute("SELECT * FROM CommuteTimes")
            return tuple(rows)
        except Exception as e:
            print('Error getting data from database:', e)