"""
Scenario: Movie Watchlist Analysis (List & Dictionary & Filter)
Question: You have a list that holds the names and IMDb scores of the movies you have watched. Write a function; this function should return a new list containing only the movies with a score higher than the value entered by the user.

movies = [
    {"title": "Inception", "score": 8.8},
    {"title": "Interstellar", "score": 8.6},
    {"title": "The Dark Knight", "score": 9.0},
    {"title": "Tenet", "score": 7.4}
]
"""

movies = [
    {"title": "Inception", "score": 8.8},
    {"title": "Interstellar", "score": 8.6},
    {"title": "The Dark Knight", "score": 9.0},
    {"title": "Tenet", "score": 7.4}
]

def filter_top_movies(movie_list, min_score):
    new_list = []
    for i in movie_list:
        if i["score"] >= min_score:
            new_list.append(i)
    return new_list       

print(filter_top_movies(movies, 8.8))