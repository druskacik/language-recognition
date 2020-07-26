from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import tensorflow as tf

from vectorizer import create_vectorizer, create_data, vec_to_categories

data = pd.read_excel('data/combined.xlsx')

corpus = data['text'].values
corpus[pd.isnull(corpus)] = ''
corpus = corpus.tolist()

labels = data['language'].values.tolist()

vectorizer, ngram_counts, vocabulary = create_vectorizer(corpus)
X, Y = create_data(ngram_counts, vocabulary, labels)

print(X[0].shape)