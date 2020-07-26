import os
import pandas as pd

from save_to_excel import save_combined

def combine_data(langs):
  data = []

  for lang in langs:
    file_list = os.listdir('data/' + lang)
    for filename in file_list:
      df = pd.read_excel('data/' + lang + '/' + filename)
      for i, row in df.iterrows():
        data.append([row['text'], row['language']])

  save_combined(data)

languages = [
  'slovak',
  'english',
  'french'
]

combine_data(languages)
