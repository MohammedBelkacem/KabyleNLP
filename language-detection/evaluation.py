from nltk.collocations import BigramCollocationFinder
import re
import codecs
import numpy as np
import string

def test_language(path,language,total):
    tp = 0
    fp = 0
    lang_name = ["kabyle","French","English","Catalan","Italian","Spanish"]
    model = [np.load(lang+".npy",allow_pickle=True) for lang in lang_name]

    with codecs.open(path,"r","utf-8") as filep:
        translate_table = dict((ord(char), None) for char in string.punctuation)
        for l,line in enumerate(filep):

            line = " ".join(line.split()[1:])
            line = line.lower()
            line = re.sub(r"\d+", "", line)
            line = line.translate(translate_table)

            finder = BigramCollocationFinder.from_words(line)

            freq_sum = np.zeros(6)
            for k,v in finder.ngram_fd.items():
                isthere = 0
                for i,lang in enumerate(lang_name):
                    for key,f in model[i]:
                        if k == key:
                            freq_sum[i] = freq_sum[i]+(f*10000)/total[i]
                            isthere = 1
                            break
                    if isthere == 0:
                        freq_sum[i] = freq_sum[i] + 1

            max_val = freq_sum.max()
            index= freq_sum.argmax()
            if max_val != 0:
                if lang_name[index] == language:
                    tp = tp + 1
                else:
                    fp = fp + 1
            print ("tp = ",tp,"fp = ",fp,freq_sum)
    print ("True Positive = ",tp)
    print ("False Positive = ",fp )

if __name__ == "__main__":
    root = ""
    lang_name = ["kabyle","French","English","Catalan","Italian","Spanish"]

    no_of_bigms = []
    for i,lang in enumerate(lang_name):
        model = np.load(lang+".npy",allow_pickle=True)
        total = 0
        for key,v in model:
            total = total + v
        no_of_bigms.append(total)
        print (total)

    train_lang_path = ["testkab.txt","testfr.txt","testen.txt","testca.txt","testit.txt","testes.txt"]
    for i,p in enumerate(train_lang_path):
        print ("Testing of ",lang_name[i])
        test_language(root+p,lang_name[i],no_of_bigms)