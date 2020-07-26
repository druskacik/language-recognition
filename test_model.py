import tensorflow as tf
import numpy as np

from vectorizer import VECTORIZER

model = tf.keras.models.load_model('saved_model/full')

categories = [
  'slovak',
  'english',
  'french'
]

def test_string(s, vectorizer):
    V = vectorizer.transform([s]).toarray()
    p = model(V.reshape(1, 1, V.shape[1]))
    predictions = tf.nn.softmax(p).numpy()
    print(predictions)
    print(categories[np.argmax(predictions)])

s1 = 'narodil som sa v roku'

test_string(s1, VECTORIZER)