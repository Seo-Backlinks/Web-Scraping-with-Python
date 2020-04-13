#Import Liberaries
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#Connect to the website
res = requests.get("https://www.dcrustedp.in/show_chart.php")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))

#Print the table
print( tabulate(df[0], headers='keys', tablefmt='psql') )
