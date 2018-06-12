import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import os
import tempfile
TEMP_FOLDER = "c:/tal/"
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))
from gensim import corpora

stoplist =['...',',',';','?','!',':','"','(',')','*','_','.','[',']','{','}','«','»','+','=','“','”']
for i in open("c:/tal/affixescolles.txt",encoding='utf-8'):
    a=i
    a=a.replace("\ufeff","")
    a=a.replace("\n","")
    stoplist.append(a)

amenzu=0
documents=[]
text=""
for izirig in open("c:/tal/arewway.txt",encoding='utf-8'):
     izirig=izirig.replace("\n"," ")
     text=text+" "+ izirig
#print(text)
h= open("c:/tal/original_text.txt","w+",encoding='utf-8')
h.write(text)
h.close()
