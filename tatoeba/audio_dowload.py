import csv
import wget
import numpy as np


files=[]
kab_audio="sentences_with_audio.csv" #afaylu n wuttunen n yimeslawen

audio_sentences=[]
with open(kab_audio, 'r') as f:
 wines = list(csv.reader(f, delimiter="\t"))

for i in wines:
        audio_sentences.append(int(i[0]))





kab="C:/tal/tatobapairs/sentences_kab.csv" # afaylu n tefyar n teqbaylit

i=0
kab_sentences=[]
with open(kab, 'r',encoding='utf-8') as f:
 wines = list(csv.reader(f, delimiter="\t"))

for i in wines:
        kab_sentences.append(int(i[0]))


import sortednp as snp

a = np.array(audio_sentences)
b = np.array(kab_sentences)

urls = snp.intersect(a, b)
print(urls)
link="https://audio.tatoeba.org/sentences/kab/"

for url in urls:
 file=link+str(url)+".mp3"
 try:

    wget.download(file)
 except:
    print(file)
