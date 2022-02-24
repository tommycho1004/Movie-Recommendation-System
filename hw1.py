#Tommy Cho, Jennifer Xin 

import sys
import math
from collections import defaultdict
from collections import Counter

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    output = {}
    movieRatingPair = [] # a list that stores only the movie and its rating from the input file
    for line in open(f): #converting each line in the input file to our desired format
        movie, rating, uid = line.split('|')
        movieRatingPair.append([movie, float(rating)])
    for movie in movieRatingPair: #appending to output dictionary
        if movie[0] not in output:
            output [movie[0]] = []
        output [movie[0]].append(movie[1])
    return output
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    output = {}
    for line in open(f): #converting each line in the input file to our desired format
        genre, mid, movie = line.split('|')
        output[movie.strip()] = genre #appending each movie, genre pair into the output dictionary
    return output
    

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    output = {}
    for mtg in d.keys(): #mtg here is for movie to genre
        movie = d[mtg]
        if not movie in output.keys(): #if the genre is not in the dictionary yet, create a new key
            output[movie] = []        
        output[movie].append(mtg) 
    return output

    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    output = {}
    for key in d.keys():
                avg = sum(d[key])/len(d[key])
                output[key] = avg
    return output

    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    sorted_dlist = sorted(d.items(),key = lambda x:x[1], reverse=True) #use d as list, sort, then convert back to dict
    sorted_ddict = sorted_dlist[:n]
    output = dict(sorted_ddict)

    return output

    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    return
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    return
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    return
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    return

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    # WRITE YOUR CODE BELOW
    return
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    return
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    return

# -------- main function for your testing -----
def main(argv):
    # write all your test code here
    # this function will be ignored by us when grading
    m_ratings = str(argv[1])
    m_movies = str(argv[2])
    print("#1.1 read_ratings_data() => movie to ratings dict \n")
    movie_rat = read_ratings_data(m_ratings)
    print(movie_rat)
    print("\n #1.2 read_movie_genre() => movie to genre dict \n")
    movie_gen = read_movie_genre(m_movies)
    print(movie_gen)
    print("\n #2.1 create_genre_dict() => genre to movies dict \n")
    gen_movie = create_genre_dict(movie_gen)
    print(gen_movie)
    print("\n #2.2 calculate_average_rating() => movie to average rating \n")
    movie_avg = calculate_average_rating(movie_rat)
    print(movie_avg)
    print("\n #3.1 get_popular_movies() => top n movies \n")
    top_movies = get_popular_movies(movie_avg, 2)
    print(top_movies)
    return
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions

    
# program will start at the following main() function call
# when you execute hw1.py
main(sys.argv)
