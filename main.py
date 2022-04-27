import markovify
import requests
from bs4 import BeautifulSoup


#Scrape Text
url = "https://www.gameblog.fr/jeu-video/jeux/tests/test-de-elden-ring-une-merveilleuse-synthese-des-jeux-from-software-en-monde-ouvert-398335"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.find_all('p')

url_two = "https://www.jeuxactu.com/test-elden-ring-alors-non-ce-n-est-pas-lui-le-goty-2022-126900.htm"
website = requests.get(url_two)
parser = BeautifulSoup(website.content, 'html.parser')
texte = parser.find_all('p')

with open("review.txt", "w") as f:
  f.write(str(text))
  f.write(str(texte))
#Scrape Text


#Generate text
with open("review.txt", "r") as f:
  review = f.read()

model = markovify.Text(review)

for i in range(30):
  print(model.make_sentence())
#Generate text
