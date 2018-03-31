'''
Created on 18-Mar-2018

@author: DELL
'''

import matplotlib.pyplot as plt
import read_files
import math
import matplotlib
import numpy

def movies_per_year_line():
    movie_list = read_files.get_movie_list()
    movies_per_year_dict = {}
    
    for x in movie_list:
        movies_per_year_dict[int(x.get_release_year())] = 0
    
    for x in movie_list:
        y = movies_per_year_dict.get(int(x.get_release_year()))
        y += 1
        movies_per_year_dict[int(x.get_release_year())] = y
    
    print(movies_per_year_dict)
    
    x = movies_per_year_dict.keys()
    y = movies_per_year_dict.values()
    
    ## Display only integers on the axes
    #yint = range(math.floor(min(y)), math.ceil(max(y))+1)
    #matplotlib.pyplot.yticks(yint)
    #xint = range(math.floor(min(x)), math.ceil(max(x))+1)
    #matplotlib.pyplot.xticks(xint)
    
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.grid(True, 'both', 'both')
    plt.plot(x, y)
    plt.show()

def total_overseas_and_us_revenue_per_year():
    movie_list = read_files.get_movie_list()
    overseas_and_us_revenue_per_year = {}
    
    for x in movie_list:
        overseas_and_us_revenue_per_year[int(x.get_release_year())] = [0, 0]
    
    for x in movie_list:
        movie_release_year = int(x.get_release_year())
        
        if hasattr(x, "overseas_in_mill_dollars"):
            movie_overseas_revenue = x.overseas_in_mill_dollars
        else:
            movie_overseas_revenue = 0
        if hasattr(x, "us_in_mill_dollars"):
            movie_us_revenue = x.us_in_mill_dollars
        else:
            movie_us_revenue = 0
        
        cumulative_overseas_revenue = overseas_and_us_revenue_per_year[movie_release_year][0]
        cumulative_overseas_revenue += movie_overseas_revenue
        cumulative_us_revenue = overseas_and_us_revenue_per_year[movie_release_year][1]
        cumulative_us_revenue += movie_us_revenue
        overseas_and_us_revenue_per_year[movie_release_year] = [cumulative_overseas_revenue, cumulative_us_revenue]
    
    print(overseas_and_us_revenue_per_year)
    
    # X = overseas_and_us_revenue_per_year.keys() ## Returns a dict_keys object
    X = list(overseas_and_us_revenue_per_year.keys())
    movie_dict_values = list(overseas_and_us_revenue_per_year.values())
    Y,Z = [],[]
    for x in movie_dict_values:
        Y.append(x[0])
        Z.append(x[1])
    print("X = " + str(X))
    print("Y = " + str(Y))
    print("Z = " + str(Z))
    
    plt.bar(X, Y, color='r', width=0.4, label="Overseas Revenue")
    temp_X = []
    for x in X:
        temp_X.append(x+0.4) 
    plt.bar(temp_X, Z, color='g', width=0.4, label="US Revenue")
    
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Overseas and US revenue in Million Dollars")
    plt.grid(True, 'both', 'both')
    
    plt.show()

def gross_revenue_rating_scatter():
    movie_list = read_files.get_movie_list()
    movie_gross_revenue_rating_dict = {}
    
    for x in movie_list:
        if hasattr(x, "gross_in_mill_dollars"):
            movie_gross_revenue_rating_dict[x.movie_id] = [x.gross_in_mill_dollars, x.get_average_rating()]
    # print(movie_gross_revenue_rating_dict)
    
    area = []
    for x in movie_gross_revenue_rating_dict:
        temp_area = movie_gross_revenue_rating_dict[x][0] * movie_gross_revenue_rating_dict[x][1]
        area.append(temp_area * 0.01)
    # print(area)
    
    X, Y, temp_values_list = [], [], []
    temp_values_list = list(movie_gross_revenue_rating_dict.values())
    for x in temp_values_list:
        X.append(x[0])
        Y.append(x[1])
    # print(X)
    # print(Y)
    
    plt.xlabel("Gross Revenue in Million Dollars")
    plt.ylabel("Average Rating")
    color = numpy.random.rand(len(movie_gross_revenue_rating_dict))
    plt.scatter(x=X, y=Y, s=area, c=color, alpha=0.5)
    plt.show()
    
# movies_per_year_line()
# total_overseas_and_us_revenue_per_year()
# gross_revenue_rating_scatter()