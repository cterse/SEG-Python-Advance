'''
Created on 31-Mar-2018

@author: DELL
'''
from builtins import int
import plot_graphs

while True:
    print("\n1 - Movies Per Year - Line Graph")
    print("2 - Total Overseas and US Revenues Per Year - Double Bar Graph")
    print("3 - Overseas and Ratings Scatter Plot")
    print("4 - Exit")
    choice = int(input("Enter your choice: "))
    
    if choice is 4:
        break
    elif choice is 1:
        plot_graphs.movies_per_year_line()
    elif choice is 2:
        plot_graphs.total_overseas_and_us_revenue_per_year()
    elif choice is 3:
        plot_graphs.gross_revenue_rating_scatter()
    else:
        print("Incorrect option! Please provide correct choice!")
    
print("Thank You!")
    
    