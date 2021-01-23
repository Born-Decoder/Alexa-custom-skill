# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:43:35 2020

@author: sandh
"""
#importing dataset

import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

dataset = load_files(r"D:\Assignment and other works\Data sets\definition_classification")
X, y = dataset.data, dataset.target



documents = []


for sen in range(0, len(X)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))
    
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)
    
    # Converting to Lowercase
    document = document.lower()
    
    # Lemmatization
    document = document.split()

    document = ' '.join(document)
    
    documents.append(document)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(X)
vectorizer.transform(X).toarray()
print(vectorizer.vocabulary_)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=13)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(X_train)
X_train = vectorizer.transform(X_train)
X_test  = vectorizer.transform(X_test)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print("Accuracy:", score)
ans = classifier.predict(X_test)
print("prediction", ans)
print("\n Actual" , y_test)
sen = ["Hello, this is not a definition yet ironically, this is!"]
print(sen)
sen = vectorizer.transform(sen)
print(classifier.predict(sen))

sen = ["I am speed"]
print(sen)
sen = vectorizer.transform(sen)
print(classifier.predict(sen))

sen = ["This is awesome"]
print(sen)
sen = vectorizer.transform(sen)
print(classifier.predict(sen))

sen = ["Without names we are fantasizing, dancing like flames, mesmerizing; my dark disquiet singing such eerie harmonies"]
print(sen)
sen = vectorizer.transform(sen)
print(classifier.predict(sen))






