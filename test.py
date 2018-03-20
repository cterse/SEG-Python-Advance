'''
Created on 18-Mar-2018

@author: DELL
'''

import matplotlib.pyplot as plt
import read_files
import math
import matplotlib

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

plt.plot(x, y)
plt.show()