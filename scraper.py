import requests
from bs4 import BeautifulSoup

webpage = 'https://sophiesfloorboard.blogspot.com/'
response = requests.get(webpage)

bs = BeautifulSoup(response.text, 'html.parser')

javascript = bs.find_all('script', attrs={'type': 'text/javascript'})

print(javascript)
