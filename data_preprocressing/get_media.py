import requests
from bs4 import BeautifulSoup

from save_to_excel import save_data

# aktuality
def get_aktuality():
  url = 'https://aktuality.sk'
  response = requests.get(url)
  text = response.text

  soup = BeautifulSoup(text)

  titles = soup.findAll('a', {
    'class': 'article-title'
  })

  titles = [t.text.strip() for t in titles]

  save_data(titles)

def get_n():
  url = 'https://dennikn.sk'
  response = requests.get(url)
  text = response.text

  soup = BeautifulSoup(text)

  titles = soup.findAll('span')

  titles = [t.text.strip() for t in titles if len(t.text.strip()) > 15]

  save_data(titles)