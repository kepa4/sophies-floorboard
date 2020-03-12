import requests
from bs4 import BeautifulSoup
import re

webpage = 'https://sophiesfloorboard.blogspot.com'
response = requests.get(webpage)

bs = BeautifulSoup(response.text, 'html.parser')

links = bs.find_all('ul', 'posts')
print(links)
