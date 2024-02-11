from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import dateparser # $ pip install dateparser

req = Request('https://www.engie.be/fr/energie/electricite-gaz/prix-conditions/parametres-indexation/parametres-indexation-electricite/', headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req).read()

soup = BeautifulSoup(html_page, 'html.parser')

values =[]
dates=[]

for  EpexDamValue in soup.select('div[class*="table_cell cell5"]'):
    value = " ".join(EpexDamValue.get_text().replace("Epex DAM", "").replace(",",".").split())
    if(value==''):
        value=0
    else:
        value=float(value)    
    values.append(value)

for  EpexDamValue in soup.select('div[class*="table_cell cell1"]'):
    date=" ".join(EpexDamValue.get_text().split())
    dt = dateparser.parse(date)
    dates.append(dt)

res = {dates[i]: values[i] for i in range(10)}
 
print("Dictionary is : " + str(res))