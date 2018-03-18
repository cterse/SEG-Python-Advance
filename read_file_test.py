'''
Created on Mar 16, 2018

@author: 10643275
'''

import Movie
from xlrd import open_workbook
from xlrd.xldate import xldate_as_tuple, xldate_from_date_tuple,\
    xldate_from_datetime_tuple, xldate_as_datetime
from datetime import datetime
 
# Convert the .csv file to .xlsx, since xlrd only supports .xls and .xlsx files
# FUTURE SCOPE. For now, convert the below files explicitly and use...

movies_list = []
# Read the .xlsx files and populate movies_list list
wb = open_workbook('Movie-Data.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_cols = sheet.ncols
    # print("No. of rows and cols: " + str(number_of_rows) + "," + str(number_of_cols))
    
    date_tuple = xldate_as_tuple(sheet.cell(1,4).value, wb.datemode)
    print(date_tuple[0])
    #print(xldate_from_date_tuple(date_tuple, wb.datemode))
    datetime_from_xldate = xldate_as_datetime(sheet.cell(1,4).value, wb.datemode)
    print(type(datetime_from_xldate))
    
    for row in range(1, number_of_rows):
        values = []
        for col in range(0, number_of_cols):
            values.append(sheet.cell(row, col).value)
        movies_list.append(Movie.Movie.create_movie_from_datafile(values))
    # print(len(movies_list))    # 608

wb = open_workbook('Movie-Ratings.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_cols = sheet.ncols
    # print("No. of rows and cols: " + str(number_of_rows) + "," + str(number_of_cols))
    
    for row in range(1, number_of_rows):
        values = []
        for col in range(0, number_of_cols):
            values.append(sheet.cell(row, col).value)
        movies_list.append(Movie.Movie.create_movie_from_ratingsfile(values))
    print(len(movies_list))    # 559

