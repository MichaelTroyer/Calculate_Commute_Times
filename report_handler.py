# -*- coding: utf-8 -*-
"""
Created on Sat June 29th 21:49 2019
@author: michael
"""


from database_handler import Database


def get_data(database, start_date=None, end_date=None):
    """
    Return data from database between start_date and end_date
    """
    data = database.get_data(start_date=start_date, end_date=end_date)
    return data


def plot_data(data):
    #TODO:
    pass
        