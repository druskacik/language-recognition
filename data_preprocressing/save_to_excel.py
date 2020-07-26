import os
import pandas as pd

def save_data(data, lang):
  data = [[text, lang] for text in data]
  df = pd.DataFrame(data, columns = ['text', 'language'])
  file_path = 'data/' + lang + '/data' + str(len(os.listdir('data/' + lang))) + '.xlsx'
  df.to_excel(file_path)
  print('Successfully saved to {} !'.format(file_path))

def save_combined(data):
  df = pd.DataFrame(data, columns = ['text', 'language'])
  file_path = 'data/combined.xlsx'
  df.to_excel(file_path)
  print('Successfully saved to {} !'.format(file_path))
