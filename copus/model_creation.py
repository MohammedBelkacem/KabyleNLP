from nltk.tag.perceptron import PerceptronTagger
import pickle
tagger = PerceptronTagger(load=False)
kab_tags_words1= [ ]
aḍris=[]
amenzu=0

#Construction de la chaine d'apprentissage à partir du corpus kabyle
for izirig in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    if (amenzu!=0):

     #ligne=ligne.lower()
     amenzu=1
     izirig=izirig.replace("\n","")
     a=izirig.split(" ")

     for i in a:
        b=i.split("/")
        if (b[1]!='NMP'):
            b[0]=b[0].lower()

        kab_tags_words1.append( (b[0], b[1]) )
     aḍris.append(kab_tags_words1)
    else:
        amenzu=1

#entrainer l'algorithme sur la base du corpus et enregistrer le modèle

trained_model="c:/tal/trained_model2.pickle"
tagger.train(aḍris,save_loc=trained_model,nr_iter=10)
