import requests
from bs4 import BeautifulSoup


def scrape_imdb_movies():
    # Send a GET request to the IMDb website
    response = requests.get('https://www.imdb.com/chart/top')

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all movie entries in the table
    movie_entries = soup.select('.lister-list tr')

    # Iterate over the movie entries and extract relevant information
    movies = []
    for entry in movie_entries:
        title_column = entry.find('td', class_='titleColumn')
        rating_column = entry.find('td', class_='ratingColumn')

        # Extract movie title, release year, and rating
        title = title_column.a.text
        year = title_column.span.text.strip('()')
        rating = rating_column.strong.text

        # Create a dictionary for each movie and append it to the list
        movie = {'title': title, 'year': year, 'rating': rating}
        movies.append(movie)

    return movies


# Call the function to scrape IMDb's top movies
movies = scrape_imdb_movies()

# Print the collected data
for movie in movies:
    print(movie)
