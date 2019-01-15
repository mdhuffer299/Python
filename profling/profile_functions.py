# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:16:48 2019

@author: C243284
"""

import pandas as pd
import statistics as stat

def missing_stat(df, column):
    # Create an empty list to store values
    row_list = []
    
    # Capture various missing and non-missing values values of a column
    column_name = column
    missing_values = sum(df[column].isnull() == True)
    non_missing_values = sum(df[column].isnull() == False)
    total_values = missing_values + non_missing_values
    missing_pct = missing_values/total_values
    non_missing_pct = 1 - missing_pct
    
    # Create List of values
    row_list.append(column_name)
    row_list.append(missing_values)
    row_list.append(non_missing_values)
    row_list.append(total_values)
    row_list.append(missing_pct)
    row_list.append(non_missing_pct)
    
    return(row_list)

def summary_stat(df, column):
    row_list = []
    values = df[column].tolist()
    
    try:
        if(df.dtypes[column] == 'float64' or df.dtypes[column] == 'int64'):
            column_name = column
            
            column_mean = stat.mean(values)
            
            column_sd = stat.stdev(values)
            column_min = min(values)
            column_max = max(values)
            column_median = stat.median(values)
            column_mode = stat.mode(values)
        elif(df.dtypes[column] == 'object'):
            column_name = column
    
            sorted_column = sorted(values)
        
            column_mean = None
            column_sd = None
            column_min = sorted_column[0]
            column_max = sorted_column[-1]
            column_median = None
            column_mode = None
        
        row_list.append(column_name)
        row_list.append(column_mean)
        row_list.append(column_sd)
        row_list.append(column_min)
        row_list.append(column_max)
        row_list.append(column_median)
        row_list.append(column_mode)
    
        return(row_list)
    except:
        row_list = [column,0,0,0,0,0,0]
        return(row_list)
