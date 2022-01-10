# -*- coding: utf-8 -*-
"""Automatisation of the preprocessing (link to the time) """

import pandas as pd 
import numpy as np
from datetime import *

# adding real starting time to the dataset
def start_time(FILE,room,df):
    
    ''' 
        INPUT: The file , room , and the df of the subject 
        OUTPUT: The real time line base on the frame recolted with the software Openface in the dataset df
        
    '''
    # getting the file 
    FILESTART = FILE.replace(".csv", "_of_details.txt")
    TXTFILE = str(room)+"_txt_file_in_csv.csv"
    dftxt = pd.read_csv(TXTFILE, sep=';', engine='python')

    # getting the parameters
    
    timeCSV = dftxt["time"][dftxt['File_name'] == FILESTART].values
    yearCSV = dftxt["year"][dftxt['File_name'] == FILESTART].values
    monthCSV = dftxt["month"][dftxt['File_name'] == FILESTART].values
    dayCSV = dftxt["day"][dftxt['File_name'] == FILESTART].values

    # month to number
    
    if str(monthCSV[0]) == "May":
        month = str(monthCSV[0]).replace("May", "5")
    elif str(monthCSV[0]) == "Jun":
        month = str(monthCSV[0]).replace("Jun", "6")
    elif str(monthCSV[0]) == "Jul":
        month = str(monthCSV[0]).replace("Jul", "7")

    total = str(yearCSV[0]) + '-' + month + '-' + str(dayCSV[0]) + ' ' + timeCSV[0]

    # getting the starting time in the good format
    
    date_format_str = '%Y-%m-%d %H:%M:%S'
    startTIME = datetime.strptime(total, date_format_str)
    
    # insert timeline in the dataset from the time start
    df.insert(0, 'time', startTIME)
    df.time= df.apply(lambda x: pd.to_datetime(x.time)+pd.Timedelta(x[' timestamp'],unit='second',) ,axis = 1)
    return df




