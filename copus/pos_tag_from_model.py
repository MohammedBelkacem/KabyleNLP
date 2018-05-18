from nltk.tag.perceptron import PerceptronTagger
import pickle
kab_tags_words1= [ ]
aḍris=[]
amenzu=0


suffixe=[]
prefixe=[]

Ponctuation=['...',',',';','?','!',':','"','(',')','*','_','.']
for i in open("c:/tal/affixescolles.txt",encoding='utf-8'):
    a=i
    a=a.replace("\ufeff","")
    a=a.replace("\n","")
    if (a[len(a)-1]=="-"):

     prefixe.append(str(a))
    else:
       suffixe.append(str(a))

def tokenize_word(word,suffixe,prefixe):
    a=''
    morpheme=word[0:word.find('-')+1]

    lemtized_word=''
    if (morpheme in prefixe):
        word=word[word.find('-')+1:len(word)]
        lemtized_word=lemtized_word+' '+morpheme
        while word.find('-')>=0:

            morpheme=word[0:word.find('-')+1]
            word=word[word.find('-')+1:len(word)]
            lemtized_word=lemtized_word+' '+morpheme
        lemtized_word=lemtized_word+' '+word
    else:
        morpheme=word[0:word.find('-')]
        lemtized_word=lemtized_word+' '+morpheme
        word=word[word.find('-')+1:len(word)]
        while word.find('-')>=0:

           morpheme=word[0:word.find('-')]
           lemtized_word=lemtized_word+' '+'-'+morpheme
           word=word[word.find('-')+1:len(word)]
        if ('-'+word in suffixe):
         lemtized_word=lemtized_word+' '+'-'+word
        else:
         lemtized_word=lemtized_word+' '+'-'+' '+word



    return lemtized_word


def tokenize(sentence,suffixe,prefixe):
       a=sentence.split()
       sentence1=""
       for i in a: #mots
        if(i.find('-')<0):
            sentence1=sentence1+' '+i
        else:
            words=tokenize_word(i,suffixe,prefixe)
            sentence1=sentence1+' '+words
       sentence1=sentence1.strip()
       return sentence1


#load the model
trained_model="file:///c:/tal/trained_model1.pickle"
tagger = PerceptronTagger()
tagger.load(trained_model)


f= open("c:/tal/tokenized_text.txt","w+",encoding='utf-8')
h= open("c:/tal/tagged_text.txt","w+",encoding='utf-8')
g=open("c:/tal/brut_text.txt",encoding='utf-8')
for line in g:
    print (line)
    for i in Ponctuation:

        if i=='.':
            line=line.replace(i,' '+i+' ')
        else:
            line=line.replace(i,' '+i+' ')
    line=line.replace("\ufeff","")
    ligne=tokenize(line,suffixe,prefixe)

    ligne=ligne.replace("  "," ")
    ligne=ligne.lower()
    #tag the tokennized sentence
    a=tagger.tag(ligne.split())
    izirig=""
    izirig1=ligne

    for u in a:
        yy=u[0]+'/'+u[1]
        izirig=izirig+yy+" "
    #generate the tagged sentence
    f.write(izirig1.lower()+'\n')
    #generate the tokennized sentence
    h.write(izirig.lower()+'\n')

f.close()
g.close()
h.close()
