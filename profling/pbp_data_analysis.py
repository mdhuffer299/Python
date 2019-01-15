# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:20:31 2019

@author: C243284
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import profile_functions as pf

df = pd.read_csv(r'C:\Users\C243284\Desktop\pbp_2009.csv', sep = ",")

column_headers = list(df)

# Create the data frame to append values to
missing_df = pd.DataFrame(columns = ['column_name', 'missing_values', 'non_missing_values', 'total_values', 'missing_pct', 'non_missing_pct'])
    
# Create the data frame to append values to
stat_df = pd.DataFrame(columns = ['column_name', 'column_mean', 'column_sd', 'column_min', 'column_max', 'column_median', 'column_mode'])

for i in column_headers:
    row_list = pf.missing_stat(df, i)
    missing_df = missing_df.append({'column_name': row_list[0], 'missing_values': row_list[1], 'non_missing_values': row_list[2], 'total_values': row_list[3], 'missing_pct': row_list[4], 'non_missing_pct': row_list[5]}, ignore_index = True)

for i in column_headers:
    row_list = pf.summary_stat(df, i)
    stat_df = stat_df.append({'column_name': row_list[0], 'column_mean': row_list[1], 'column_sd': row_list[2], 'column_min': row_list[3], 'column_max': row_list[4], 'column_median': row_list[5], 'column_mode': row_list[6]}, ignore_index = True)
