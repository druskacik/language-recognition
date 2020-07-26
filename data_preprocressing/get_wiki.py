import requests
from bs4 import BeautifulSoup

from save_to_excel import save_data
from split_into_sentences import split_into_sentences

def get_wiki(url, lang, number_of_requests=100):
  sentences = []
  for i in range(number_of_requests):
    response = requests.get(url)
    text = response.text

    soup = BeautifulSoup(text)

    paragraphs = soup.findAll('p')

    paragraphs = [remove_quotations(p.text.strip()) for p in paragraphs]

    for p in paragraphs:
      paragraph_sentences = split_into_sentences(p)
      paragraph_sentences = [s for s in paragraph_sentences if len(s) > 5]
      for s in paragraph_sentences:
        sentences.append(s)

    print('Request No. {}, sentences: {}'.format(i, len(sentences)))
  
  save_data(sentences, lang)

def remove_quotations(text):
  stripped_text = ''
  append = True
  for letter in text:
    if letter == '[':
      append = False
    if append:
      stripped_text += letter
    if letter == ']':
      append = True
  return stripped_text

url_sk = 'https://sk.wikipedia.org/wiki/%C5%A0peci%C3%A1lne:N%C3%A1hodn%C3%A1'
url_en = 'https://en.wikipedia.org/wiki/Special:Random'
url_fr = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

get_wiki(url_sk, 'slovak', 300)
get_wiki(url_en, 'english', 200)
get_wiki(url_fr, 'french', 200)
