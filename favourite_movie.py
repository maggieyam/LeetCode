'''
At Facebook, every person has a list of friends 
and a list of movies that they like
Using OOP, write a function which finds for a particular person the most popular movie among his/her network of friends

1. person -> friends (an array)
          -> movies (an array)
2. friends most frequent movie

'''
from collections import defaultdict
from collections import deque 

class Person:
    def __init__(self, name, friends=[], movies=[]):
        self.name = name
        self.friends = friends
        self.movies = movies

def most_popular_movie(person):        
    movie_freq = count_movies_freqs(person) # freq = {star_wars: 1000, lion_king: 999, Raya: 500...}
    maximum = -inf
    fav_movies = []

    for movie, count in movie_freq.items():
        if count > maximum:
            fav_movies = [movie]
            maximum = count
        elif count == maximum:
            fav_movies.append(movie)
     
    return fav_movie

def count_movies_freqs(person):
    freq = defaultdict(int)
    network = deque([person])
    visited = set()

    while network:
        ppl = queue.popleft()
        visited.add(ppl)
        
        for movie in ppl.movies:
            freq[movie] += 1

        for friend in ppl.friends:
            if friend not in visited:
                network.append(friend)
    return freq

