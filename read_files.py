'''
Created on Mar 16, 2018

@author: 10643275
'''

import Movie
from xlrd import open_workbook
from xlrd.xldate import xldate_as_tuple, xldate_from_date_tuple,\
    xldate_from_datetime_tuple, xldate_as_datetime
from datetime import datetime
from builtins import str
from _ast import Str
 
# Convert the .csv file to .xlsx, since xlrd only supports .xls and .xlsx files
# FUTURE SCOPE. For now, convert the below files explicitly and use...

def get_movie_list():
    movies_list = []
    # Read the .xlsx files and populate movies_list list
    wb = open_workbook('Movie-Data.xlsx')
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_cols = sheet.ncols
        # print("No. of rows and cols: " + str(number_of_rows) + "," + str(number_of_cols))
        
        for row in range(1, number_of_rows):
            values = []
            for col in range(0, number_of_cols):
                value = sheet.cell(row, col).value
                if col == 4:
                    value = xldate_as_datetime(value, wb.datemode)
                    value = str(value.date()).replace('-','/').strip()
                elif col == 0 or col == 1 or col == 2 or col == 3 or col == 5:
                    value = str(value).strip()
                values.append(value)
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
                value = sheet.cell(row, col).value
                if col == 0 or col == 1:
                    value = str(value).strip()
                if col == 5:
                    value = str(int(value)).strip()
                values.append(value)
            movies_list.append(Movie.Movie.create_movie_from_ratingsfile(values))
    
    # print("Total movies = " + str(len(movies_list)))    # 1167
    
    # Scan movies_list for duplicates and merge them
    count = 0
    for x in movies_list:
        for y in movies_list:
            if x is y:
                continue
            if x.equals_movie(y):
                # print(x.movie_title + "("+x.release_date+") == " + y.movie_title + "("+y.release_date+")")
                x.fill_details_from_movie(y)
                movies_list.remove(y)
                count += 1
    # print("Duplicate count = " + str(count))
    # print("Unique movies = " + str(len(movies_list)))
    
    # The final movies list is prepared. Allot movie ids to the movies
    id_numeral = 0
    for x in movies_list:
        x.movie_id = "MOV" + str(id_numeral)
        id_numeral += 1
    
    return movies_list
