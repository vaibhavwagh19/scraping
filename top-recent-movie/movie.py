import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_American_films_of_2023'

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\nTop 10 Recent Movies:\n")
        movie_elements = soup.find_all('i')
        for i, movie_element in enumerate(movie_elements):
            movie_info = movie_element.text
            print(f"{i + 1}. {movie_info}\n")
            if i == 9:  
                break
    else:
        print(f'Failed to fetch data from Wikipedia. Status code: {response.status_code}')

except Exception as e:
    print(f'An error occurred: {str(e)}')
