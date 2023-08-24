import requests
from bs4 import BeautifulSoup

result = requests.get("https://whitehouse.gov/briefing-room/statements-releases/")
src = result.content

soup = BeautifulSoup(src, 'lxml') 
links = soup.find_all("h2")

urls = []


for link in links:
    link = link.find('a')

    if link:
        link = link.attrs['href']
        print(link)
        urls.append(link)
    else:
        continue

print(urls)

