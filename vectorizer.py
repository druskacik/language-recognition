from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

data = pd.read_excel('data/combined.xlsx')

corpus = data['text'].values
corpus[pd.isnull(corpus)] = ''
corpus = corpus.tolist()

def create_vectorizer(corpus):
  vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
  ngram_counts = vectorizer.fit_transform(corpus)
  vocab = vectorizer.get_feature_names()
  
  return vectorizer, ngram_counts, vocab

def create_data(ngram_counts, vocabulary, labels):
  X = []
  Y = []
  labels_list = np.array(['slovak', 'english', 'french'])
  for (i, x) in enumerate(ngram_counts):
    label = np.zeros(3)
    label[labels_list == labels[i]] = 1

    X.append(x.toarray())
    Y.append(label)
  return np.array(X), np.array(Y)

def vec_to_categories(Y):
    vec = []
    for y in Y:
        val = np.where(y == 1)[0][0]
        vec.append(val)
    return np.array(vec)

VECTORIZER, ngram_counts, vocab = create_vectorizer(corpus)