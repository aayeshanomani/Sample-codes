import requests
from bs4 import BeautifulSoup

username = input('Enter username: ')

URL = "https://www.instagram.com/{}/"

r = requests.get(URL.format(username))
s = BeautifulSoup(r.text, "html.parser")
u = s.find("meta", property="og:image")
url = u.attrs['content']

with open(username+'.jpg', "wb") as pic:
    binary = requests.get(url).content
    pic.write(binary)