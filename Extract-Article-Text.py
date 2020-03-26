# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Specify the url of choice
url = "https://en.wikipedia.org/wiki/Car"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# Using Beautifulsoup to parse the html
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.find('div', {"class": "mw-parser-output"})

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text
print(article)
