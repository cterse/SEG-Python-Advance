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
        if '/' in self.release_date:
            return self.release_date.split('/')[0]
        else:
            return self.release_date
    
    def equals_movie(self, movie):
        if self.movie_title.lower() == movie.movie_title.lower() and self.get_release_year() == movie.get_release_year():
            return True
        return False
    
    def fill_details_from_movie(self, movie):
        params = Movie.get_parameter_list()
        for x in params:
            if not hasattr(self, x) and hasattr(movie, x):
                y = getattr(movie, x)
                setattr(self, x, y)
    
    @staticmethod
    def get_parameter_list():
        params = []
        params.append("movie_title")
        params.append("director")
        params.append("genre")
        params.append("release_date")
        params.append("release_day_of_week")
        params.append("studio")
        params.append("adjusted_gross_in_mill_dollars")
        params.append("budget_in_mill_dollars")
        params.append("gross_in_mill_dollars")
        params.append("imdb_rating")
        params.append("movielens_rating")
        params.append("overseas_in_mill_dollars")
        params.append("overseas_percent")
        params.append("profit_in_mill_dollars")
        params.append("profit_percent")
        params.append("runtime_in_min")
        params.append("us_in_mill_dollars")
        params.append("gross_percent_us")
        params.append("rotten_tomatoes_ratings_percent")
        params.append("audience_ratings_percent")
        return params
    
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
movie_obj.release_date = "2018/03/22"
movie_obj.movie_title = "ABC"
movie_obj2 = Movie()
movie_obj2.fill_details_from_movie(movie_obj)
movie_obj2.release_date = "2018"
# print(movie_obj.equals_movie(movie_obj2))