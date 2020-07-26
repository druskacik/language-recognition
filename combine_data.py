from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

data = pd.read_excel('data/combined.xlsx')

corpus = data['text'].values
corpus[pd.isnull(corpus)] = ''
corpus = corpus.tolist()

labels = data['language'].values.tolist()

def create_vectorizer(corpus, labels):
  vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 2))
  ngram_counts = vectorizer.fit_transform(corpus)
  vocab = vectorizer.get_feature_names()
  [X, Y] = create_data(ngram_counts, vocab, labels)

  return vectorizer, vocab, X, Y


def create_data(ngram_counts, vocabulary, labels):
  X = []
  Y = []
  labels_list = np.array(['slovak', 'english', 'french'])
  for (i, x) in enumerate(ngram_counts):
    label = np.zeros(3)
    label[labels_list == labels[i]] = 1

    X.append(x.toarray())
    Y.append(label)
  return X, Y

vectorizer, vocabulary, X, Y = create_vectorizer(corpus, labels)

