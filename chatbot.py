import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
import random
import json


stemmer=LancasterStemmer()

with open("intents.json") as f:
    data=json.load(f)

print(data["intents"])

