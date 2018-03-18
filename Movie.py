'''
Created on Mar 16, 2018

@author: 10643275
'''

class Movie:

    def get_movie_title(self):
        return self.__movie_title


    def get_director(self):
        return self.__director


    def get_genre(self):
        return self.__genre


    def get_release_date(self):
        return self.__release_date


    def get_release_day_of_week(self):
        return self.__release_day_of_week


    def get_studio(self):
        return self.__studio


    def get_adjusted_gross_in_mill_dollars(self):
        return self.__adjusted_gross_in_mill_dollars


    def get_budget_in_mill_dollars(self):
        return self.__budget_in_mill_dollars


    def get_gross_in_mill_dollars(self):
        return self.__gross_in_mill_dollars


    def get_imdb_rating(self):
        return self.__imdb_rating


    def get_movielens_rating(self):
        return self.__movielens_rating


    def get_overseas_in_mill_dollars(self):
        return self.__overseas_in_mill_dollars


    def get_overseas_percent(self):
        return self.__overseas_percent


    def get_profit_in_mill_dollars(self):
        return self.__profit_in_mill_dollars


    def get_profit_percent(self):
        return self.__profit_percent


    def get_runtime_in_min(self):
        return self.__runtime_in_min


    def get_us_in_mill_dollars(self):
        return self.__us_in_mill_dollars


    def get_gross_percent_us(self):
        return self.__gross_percent_us


    def get_rotten_tomatoes_ratings_percent(self):
        return self.__rotten_tomatoes_ratings_percent


    def get_audience_ratings_percent(self):
        return self.__audience_ratings_percent


    def set_movie_title(self, value):
        self.__movie_title = value


    def set_director(self, value):
        self.__director = value


    def set_genre(self, value):
        self.__genre = value


    def set_release_date(self, value):
        self.__release_date = value


    def set_release_day_of_week(self, value):
        self.__release_day_of_week = value


    def set_studio(self, value):
        self.__studio = value


    def set_adjusted_gross_in_mill_dollars(self, value):
        self.__adjusted_gross_in_mill_dollars = value


    def set_budget_in_mill_dollars(self, value):
        self.__budget_in_mill_dollars = value


    def set_gross_in_mill_dollars(self, value):
        self.__gross_in_mill_dollars = value


    def set_imdb_rating(self, value):
        self.__imdb_rating = value


    def set_movielens_rating(self, value):
        self.__movielens_rating = value


    def set_overseas_in_mill_dollars(self, value):
        self.__overseas_in_mill_dollars = value


    def set_overseas_percent(self, value):
        self.__overseas_percent = value


    def set_profit_in_mill_dollars(self, value):
        self.__profit_in_mill_dollars = value


    def set_profit_percent(self, value):
        self.__profit_percent = value


    def set_runtime_in_min(self, value):
        self.__runtime_in_min = value


    def set_us_in_mill_dollars(self, value):
        self.__us_in_mill_dollars = value


    def set_gross_percent_us(self, value):
        self.__gross_percent_us = value


    def set_rotten_tomatoes_ratings_percent(self, value):
        self.__rotten_tomatoes_ratings_percent = value


    def set_audience_ratings_percent(self, value):
        self.__audience_ratings_percent = value


    def del_movie_title(self):
        del self.__movie_title


    def del_director(self):
        del self.__director


    def del_genre(self):
        del self.__genre


    def del_release_date(self):
        del self.__release_date


    def del_release_day_of_week(self):
        del self.__release_day_of_week


    def del_studio(self):
        del self.__studio


    def del_adjusted_gross_in_mill_dollars(self):
        del self.__adjusted_gross_in_mill_dollars


    def del_budget_in_mill_dollars(self):
        del self.__budget_in_mill_dollars


    def del_gross_in_mill_dollars(self):
        del self.__gross_in_mill_dollars


    def del_imdb_rating(self):
        del self.__imdb_rating


    def del_movielens_rating(self):
        del self.__movielens_rating


    def del_overseas_in_mill_dollars(self):
        del self.__overseas_in_mill_dollars


    def del_overseas_percent(self):
        del self.__overseas_percent


    def del_profit_in_mill_dollars(self):
        del self.__profit_in_mill_dollars


    def del_profit_percent(self):
        del self.__profit_percent


    def del_runtime_in_min(self):
        del self.__runtime_in_min


    def del_us_in_mill_dollars(self):
        del self.__us_in_mill_dollars


    def del_gross_percent_us(self):
        del self.__gross_percent_us


    def del_rotten_tomatoes_ratings_percent(self):
        del self.__rotten_tomatoes_ratings_percent


    def del_audience_ratings_percent(self):
        del self.__audience_ratings_percent

    movie_title                         = None
    director                            = None
    genre                               = None
    release_date                        = None
    release_day_of_week                 = None
    studio                              = None
    adjusted_gross_in_mill_dollars      = None
    budget_in_mill_dollars              = None
    gross_in_mill_dollars               = None
    imdb_rating                         = None
    movielens_rating                    = None
    overseas_in_mill_dollars            = None
    overseas_percent                    = None
    profit_in_mill_dollars              = None
    profit_percent                      = None
    runtime_in_min                      = None
    us_in_mill_dollars                  = None
    gross_percent_us                    = None
    rotten_tomatoes_ratings_percent     = None
    audience_ratings_percent            = None
    
    movie_title = property(get_movie_title, set_movie_title, del_movie_title, "movie_title's docstring")
    director = property(get_director, set_director, del_director, "director's docstring")
    genre = property(get_genre, set_genre, del_genre, "genre's docstring")
    release_date = property(get_release_date, set_release_date, del_release_date, "release_date's docstring")
    release_day_of_week = property(get_release_day_of_week, set_release_day_of_week, del_release_day_of_week, "release_day_of_week's docstring")
    studio = property(get_studio, set_studio, del_studio, "studio's docstring")
    adjusted_gross_in_mill_dollars = property(get_adjusted_gross_in_mill_dollars, set_adjusted_gross_in_mill_dollars, del_adjusted_gross_in_mill_dollars, "adjusted_gross_in_mill_dollars's docstring")
    budget_in_mill_dollars = property(get_budget_in_mill_dollars, set_budget_in_mill_dollars, del_budget_in_mill_dollars, "budget_in_mill_dollars's docstring")
    gross_in_mill_dollars = property(get_gross_in_mill_dollars, set_gross_in_mill_dollars, del_gross_in_mill_dollars, "gross_in_mill_dollars's docstring")
    imdb_rating = property(get_imdb_rating, set_imdb_rating, del_imdb_rating, "imdb_rating's docstring")
    movielens_rating = property(get_movielens_rating, set_movielens_rating, del_movielens_rating, "movielens_rating's docstring")
    overseas_in_mill_dollars = property(get_overseas_in_mill_dollars, set_overseas_in_mill_dollars, del_overseas_in_mill_dollars, "overseas_in_mill_dollars's docstring")
    overseas_percent = property(get_overseas_percent, set_overseas_percent, del_overseas_percent, "overseas_percent's docstring")
    profit_in_mill_dollars = property(get_profit_in_mill_dollars, set_profit_in_mill_dollars, del_profit_in_mill_dollars, "profit_in_mill_dollars's docstring")
    profit_percent = property(get_profit_percent, set_profit_percent, del_profit_percent, "profit_percent's docstring")
    runtime_in_min = property(get_runtime_in_min, set_runtime_in_min, del_runtime_in_min, "runtime_in_min's docstring")
    us_in_mill_dollars = property(get_us_in_mill_dollars, set_us_in_mill_dollars, del_us_in_mill_dollars, "us_in_mill_dollars's docstring")
    gross_percent_us = property(get_gross_percent_us, set_gross_percent_us, del_gross_percent_us, "gross_percent_us's docstring")
    rotten_tomatoes_ratings_percent = property(get_rotten_tomatoes_ratings_percent, set_rotten_tomatoes_ratings_percent, del_rotten_tomatoes_ratings_percent, "rotten_tomatoes_ratings_percent's docstring")
    audience_ratings_percent = property(get_audience_ratings_percent, set_audience_ratings_percent, del_audience_ratings_percent, "audience_ratings_percent's docstring")
    
    def get_release_year(self):
        if '/' in self.__release_date:
            return self.__release_date.split('/')[2]
        else:
            return self.__release_date
    
    def equals(self, movie):
        #print("Comparing: "+ self.__movie_title + " with " + movie.movie_title)
        #print("Release date: " + self.get_release_year() + " x " + movie.get_release_year())
        if self.__movie_title == movie.movie_title and self.get_release_year() == movie.get_release_year():
            return True
        else: 
            return False
    
    def copy_details(self, movie):
        if self.__director == None and movie.director != None:
            self.__director = movie.director
        if self.__genre == None and movie.genre != None:
            self.__genre = movie.genre
        if self.__release_date == None and movie.release_date != None:
            self.__release_date = movie.release_date
        if self.__release_day_of_week == None and movie.release_day_of_week != None:
            self.__release_day_of_week = movie.release_day_of_week
        if self.__studio == None and movie.studio != None:
            self.__studio = movie.studio
        if self.__adjusted_gross_in_mill_dollars == None and movie.adjusted_gross_in_mill_dollars != None:
            self.__adjusted_gross_in_mill_dollars = movie.adjusted_gross_in_mill_dollars
        if self.__budget_in_mill_dollars == None and movie.budget_in_mill_dollars != None:
            self.__budget_in_mill_dollars = movie.budget_in_mill_dollars
        if self.__gross_in_mill_dollars == None and movie.gross_in_mill_dollars != None:
            self.__gross_in_mill_dollars = movie.gross_in_mill_dollars
        if self.__imdb_rating == None and movie.imdb_rating != None:
            self.__imdb_rating = movie.imdb_rating
        if self.__movielens_rating == None and movie.movielens_rating != None:
            self.__movielens_rating = movie.movielens_rating
        if self.__overseas_in_mill_dollars == None and movie.overseas_in_mill_dollars != None:
            self.__overseas_in_mill_dollars = movie.overseas_in_mill_dollars
        if self.__overseas_percent == None and movie.overseas_percent != None:
            self.__overseas_percent = movie.overseas_percent
        if self.__profit_in_mill_dollars == None and movie.profit_in_mill_dollars != None:
            self.__profit_in_mill_dollars = movie.profit_in_mill_dollars
        if self.__profit_percent == None and movie.profit_percent != None:
            self.__profit_percent = movie.profit_percent
        if self.__runtime_in_min == None and movie.runtime_in_min != None:
            self.__runtime_in_min = movie.runtime_in_min
        if self.__us_in_mill_dollars == None and movie.us_in_mill_dollars != None:
            self.__us_in_mill_dollars = movie.us_in_mill_dollars
        if self.__gross_percent_us == None and movie.gross_percent_us != None:
            self.__gross_percent_us = movie.gross_percent_us
        if self.__rotten_tomatoes_ratings_percent == None and movie.rotten_tomatoes_ratings_percent != None:
            self.__rotten_tomatoes_ratings_percent = movie.rotten_tomatoes_ratings_percent
        if self.__audience_ratings_percent == None and movie.audience_ratings_percent != None:
            self.__audience_ratings_percent = movie.audience_ratings_percent    
    
    @staticmethod
    def create_movie_from_datafile(values):
        movie_obj = Movie()
        movie_obj.release_day_of_week = values[0]
        movie_obj.director = values[1]
        movie_obj.genre = values[2]
        movie_obj.movie_title = values[3]
        movie_obj.release_date = values[4]
        movie_obj.studio = values[5]
        movie_obj.adjusted_gross_in_mill_dollars = values[6]
        movie_obj.budget_in_mill_dollars = values[7]
        movie_obj.gross_in_mill_dollars = values[8]
        movie_obj.imdb_rating = values[9]
        movie_obj.movielens_rating = values[10]
        movie_obj.overseas_in_mill_dollars = values[11]
        movie_obj.overseas_percent = values[12]
        movie_obj.profit_in_mill_dollars = values[13]
        movie_obj.profit_percent = values[14]
        movie_obj.runtime_in_min = values[15]
        movie_obj.us_in_mill_dollars = values[16]
        movie_obj.gross_percent_us = values[17]
        return movie_obj
    
    @staticmethod
    def create_movie_from_ratingsfile(values):
        movie_obj = Movie()
        movie_obj.movie_title = values[0]
        movie_obj.genre = values[1]
        movie_obj.rotten_tomatoes_ratings_percent = values[2]
        movie_obj.audience_ratings_percent = values[3]
        movie_obj.budget_in_mill_dollars = values[4]
        movie_obj.release_date = values[5]
        return movie_obj
      
movie_obj = Movie()
movie_obj.release_date = "01/02/2018"
#print(movie_obj.movie_title)