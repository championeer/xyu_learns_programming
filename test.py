import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage
simple_web_scraper('https://example.com')
