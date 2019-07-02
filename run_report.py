# -*- coding: utf-8 -*-
"""
Created on Sat June 29th 21:49 2019
@author: michael
"""

import pandas as pd
import matplotlib.pyplot as plt

from database_handler import Database


def plot_data(data):
    times = pd.to_datetime(data.Datetime)
    
    optimistic_mean = data.groupby([times.dt.hour]).Fastest.mean()
    optimistic_std = data.groupby([times.dt.hour]).Fastest.std()
    optimistic_min = data.groupby([times.dt.hour]).Fastest.min()
    optimistic_max = data.groupby([times.dt.hour]).Fastest.max()
    
    pessimistic_mean = data.groupby([times.dt.hour]).Slowest.mean()
    pessimistic_std = data.groupby([times.dt.hour]).Slowest.std()
    pessimistic_min = data.groupby([times.dt.hour]).Slowest.min()
    pessimistic_max = data.groupby([times.dt.hour]).Slowest.max()
        
    xs = optimistic_mean.index
       
    plt.figure(figsize=(12,8))
    
    plt.plot(xs, optimistic_mean, c='b', label='Optimistic Estimate')
    plt.errorbar(xs, optimistic_mean, optimistic_std,label='Optimistoc Std Dev')
    plt.fill_between(
            xs,
            optimistic_min,
            optimistic_max,
            color='b',
            alpha=0.25,
            label='Optimistic Range'
            )
    
    plt.plot(xs, pessimistic_mean, c='r', label='Pessimistic Estimate')
    plt.errorbar(xs, pessimistic_mean, pessimistic_std, label='Pessimistic Std Dev')
    plt.fill_between(
            xs,
            pessimistic_min,
            pessimistic_max,
            color='r',
            alpha=0.25,
            label='Pessimistic Range'
            )    
    
    plt.title('Average Commute Times')
    plt.ylabel('Minutes')   
    plt.xlabel('Hour of Day')
    
    plt.xticks(xs)
    plt.legend()
    
    plt.show()
    
        

def main(database, start_date=None, end_date=None, specific_route=None):
    data = database.get_data(start_date=start_date, end_date=end_date, specific_route=specific_route)
    plot_data(data)
    
    return data
