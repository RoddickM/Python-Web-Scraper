import requests
from bs4 import BeautifulSoup

result = requests.get("https://whitehouse.gov/briefing-room/statements-releases/")
src = result.content

soup = BeautifulSoup(src, 'lxml') 
links = soup.find_all("a")

for link in links:
    if "Biden" in link.text:
        print(link)
        print(link.attrs['href'])