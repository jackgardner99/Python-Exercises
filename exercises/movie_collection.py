movie_collection = []

def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)

def display_movies():
    print("Movie Catalog:")
    for title, director, year in movie_collection:
        print(f"Title: {title}, Director: {director}, Year: {year}")

add_movie("Star Wars", "George Lucas", 1970)
add_movie("IT", "Stephen King", 1988)
add_movie("Ready Player One", "Steven Spielberg", 2017)
add_movie("Shawshank Redemption", "Stephen King", 1985)
add_movie("Get Out", "Jordan Peele", 2012)
add_movie("Us", "Jordan Peele", 2016)
add_movie("Star Wars, Phantom Menace", "George Lucas", 1999)

display_movies()

def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, year = movie
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director

movies_by_spielberg = search_by_director("Steven Spielberg")
print("Movies by Steven Spielberg")
for title, director, year in movies_by_spielberg:
    print(f"Title: {title}, Year: {year}")

def remove_movie(title):
    for movie in movie_collection:
        movie_title, director, year = movie
        if movie_title.lower() == title.lower():
            movie_collection.remove(movie)

remove_movie("Star Wars")

display_movies()

def update_movie(title, new_director, new_year):
    for movie in movie_collection:
        movie_title, movie_director, movie_year = movie
        if title.lower() == movie_title.lower():
            movie_collection.remove(movie)
            new_movie = title, new_director, new_year
            movie_collection.append(new_movie)
            


update_movie("IT", "Stephen King", 1990)

display_movies()

movie_collection.sort(key=lambda movie: movie[2])
print(movie_collection)