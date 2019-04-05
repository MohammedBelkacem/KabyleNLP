from sklearn.feature_extraction.text import CountVectorizer

corpus = [
]
#Construction du texte global
first=0
for ligne in open("c:/tal/corpusnew.txt",encoding='utf-8'):
    if (first!=0):
        corpus.append(ligne)
    if first>150:
            break

    first=first+1
#print(sentences[:20])


list_1= []

first=0
for ligne in open("c:/tal/stopwords.txt",encoding='utf-8'):
    if (first!=0):
        list_1.append(ligne)
    first=1



vectorizer = CountVectorizer(stop_words=list_1)

a=vectorizer.fit_transform(corpus).todense()


print ("tafelwit: ",len(vectorizer.vocabulary_) )
#print ("awalen n uneḥbus: ",vectorizer.stop_words)

#for i in corpus:
 #   print("tafyirt: ",i)
#print(a)

import matplotlib.pyplot as plt
import numpy as np
plt.matshow(a)

plt.show()
