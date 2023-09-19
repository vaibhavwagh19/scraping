import requests
from bs4 import BeautifulSoup
import string

def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.text, 'html.parser')
    
    infobox = soup.find('table', {'class': 'infobox'})
    
    if infobox:
        rows = infobox.find_all('tr')
        for row in rows:
            heading = row.find('th')
            details = row.find('td')
            if heading and details:
                print(f"{heading.text.strip()} -> {details.text.strip()}\n")
    
    paragraphs = soup.find_all('p')[:3] 
    for paragraph in paragraphs:
        print(paragraph.text)

if __name__ == "__main__":
    enter_input = input("Enter search keyword: ")
    formatted_input = string.capwords(enter_input)
    search_terms = formatted_input.split()
    search_query = "_".join(search_terms)

    url = f"https://en.wikipedia.org/wiki/{search_query}"

    wikibot(url)
