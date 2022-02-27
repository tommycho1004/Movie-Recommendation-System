#Tommy Cho, Jennifer Xin 

import sys
import math
from collections import defaultdict
from collections import Counter
from tempfile import tempdir

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
    sorted_dlist = sorted(d.items(),key = lambda x:x[1], reverse=True) #use d as list, sort, then convert back to dict
    sorted_ddict = sorted_dlist[:n]
    output = dict(sorted_ddict)

    return output

    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    dlist = d.items()
    output_list = []
    for ele in dlist:
        x,y = ele
        if y >= thres_rating:
            output_list.append(ele)
    output = dict(output_list)
    return output
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    movies = genre_to_movies[genre]
    tmp = {}
    for ele in movie_to_average_rating.items():
        x,y = ele
        if x in movies:
            for ele2 in movies:
                if x == ele2:
                    tmp[x] = y

    return get_popular_movies(tmp,n)
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    output = 0
    movies = genre_to_movies[genre] # all movies in genre
    sum = 0
    for movie in movies:
        sum += movie_to_average_rating[movie]
    output = sum / len(movies)
    return output
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    tmp = {}
    for key in genre_to_movies.keys():
        tmp[key] = get_genre_rating(key, genre_to_movies, movie_to_average_rating)
    output = get_popular_movies(tmp,n)
    return output

# ------ TASK 4: USER FOCUSED  --------
# -- IMPORTANT: USER ID IS HANDLED AS A STRING --
# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    output = {}
    for line in open(f):
        movie, rating, uid = line.split('|')
        if uid.strip() not in output: #case where the user is not in the dictionary yet
            output[uid.strip()] = [(movie, rating)]
        else: 
            output[uid.strip()].append((movie, rating))

    return output
    
# 4.2
#returns the top genre that the user likes based on the user's ratings. 
# Here, the top genre for the user will be determined by taking the average rating of the 
# movies genre-wise that the user has rated. If multiple genres have the same highest ratings 
# for the user, return any one of genres (arbitrarily) as the top genre.
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id as a string
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    if type(user_id) == int:
        user_id = str(user_id)
    if user_id not in user_to_movies:
        return 'Invalid User ID'
    else:
        user_movieList = user_to_movies[user_id]
    genre_rating = {}
    mutableList = [] 
    for rating in user_movieList: #since tuples are immutable, we can convert the tuples of movie and rating into a mutable list
        x = list(rating)
        mutableList.append(x)
    for i in range(len(mutableList)): #convert movie and rating list into genre and rating dictionary
        mutableList[i][0] = movie_to_genre[user_movieList[i][0]]
        key, value = mutableList[i][0], float(mutableList[i][1]) #create a dictionary of genre rating pairs
        if key not in genre_rating:
            genre_rating[key] = []
        genre_rating[key].append(value)
    for item in genre_rating: #convert values of genre_rating dictionary into the average of each genre
        rlist = genre_rating.get(item)
        genre_rating[item] = sum(rlist)/len(rlist)
    sorted_genre_rating = {key: value for key, value in sorted(genre_rating.items(), key=lambda x: x[1], reverse= True)}
    
    return list(sorted_genre_rating.keys())[0]
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    if type(user_id) == int:
        user_id = str(user_id)
    gen_movie = create_genre_dict(movie_to_genre)
    fav_genre = get_user_genre(user_id,user_to_movies,movie_to_genre) # user's fav genre
    user_movs = [x for x,y in user_to_movies[user_id]] # all of user's reviewed movies
    num_mov = len(gen_movie[fav_genre]) # num movies in genre
    pop_gen = get_popular_in_genre(fav_genre,gen_movie,movie_to_average_rating, num_mov)
    output = {}
    for x in range(0,3):
        for key in pop_gen.keys():
            if key not in user_movs:
                output[key] = movie_to_average_rating[key]
    
    return output









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
    print("\n #3.2 filter_movies() => movies at or above threshold rating \n")
    fil_movies = filter_movies(movie_avg,4)
    print(fil_movies)
    print("\n #3.3 get_popular_in_genre() => top n movies in x genre \n")
    top_movies_in_genre = get_popular_in_genre("Action", gen_movie, movie_avg, 10)
    print(top_movies_in_genre)
    print("\n #3.4 get_genre_rating() => avg rating of genre \n")
    gen_rat = get_genre_rating("Adventure", gen_movie, movie_avg)
    print(gen_rat)
    print("\n #3.5 genre_popularity() => top n genres \n")
    top_gen = genre_popularity(gen_movie, movie_avg,2)
    print(top_gen)
    print("\n #4.1 read_user_ratings() => user to movies dict \n")
    user_movies = read_user_ratings(m_ratings)
    print(user_movies)
    print("\n #4.2 get_user_genre() => user's top genre \n")
    user_top_gen = get_user_genre(1,user_movies,movie_gen)
    print(user_top_gen)
    print("\n #4.3 recommend_movies() => recommend 3 top movies in genre \n")
    user_recs = recommend_movies(1, user_movies, movie_gen, movie_avg)
    print(user_recs)
    return
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions

    
# program will start at the following main() function call
# when you execute hw1.py
main(sys.argv)
