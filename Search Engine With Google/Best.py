import requests
import timeit
import html5lib # pip install html5lib
from bs4 import BeautifulSoup
import re
search = input("Search:")
results = 10
start = timeit.default_timer()
page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
soup = BeautifulSoup(page.content, "html5lib")
links = soup.findAll("a")
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        print(link.get('href').split("?q=")[1].split("&sa=U")[0])
stop = timeit.default_timer()
exitime=(stop - start)
print("______________________________________________________")
print("Result come in {} second".format(exitime))
