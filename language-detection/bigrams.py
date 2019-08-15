from nltk.collocations import BigramCollocationFinder
import re
import codecs
import numpy as np
import string

def train_language(path,lang_name):
    words_all = []
    translate_table = dict((ord(char), None) for char in string.punctuation)
    # reading the file in unicode format using codecs library
    with codecs.open(path,"r","utf-8") as filep:

        for i,line in enumerate(filep):
            # extracting the text sentence from each line
            line = " ".join(line.split()[1:])
            line = line.lower()   # to lower case
            line = re.sub(r"\d+", "", line) # remove digits

            if len(line) != 0:
                line = line.translate(translate_table) # remove punctuations
                words_all += line
                words_all.append(" ") # append sentences with space

    all_str = ''.join(words_all)
    all_str = re.sub(' +',' ',all_str) # replace series of spaces with single space
    seq_all = [i for i in all_str]

    # extracting the bi-grams and sorting them according to their frequencies
    finder = BigramCollocationFinder.from_words(seq_all)
    finder.apply_freq_filter(5)
    bigram_model = finder.ngram_fd.items()
    bigram_model = sorted(finder.ngram_fd.items(), key=lambda item: item[1],reverse=True)

    print (lang_name)
    for i in bigram_model:
        print (i)

    np.save(lang_name+".npy",bigram_model) # save language model

if __name__ == "__main__":
    root = ""
    lang_name = ["kabyle","French","English","Catalan","Italian","Spanish"]
    train_lang_path = ["kab.txt","fr.txt","en.txt","ca.txt",'it.txt','es.txt']
    for i,p in enumerate(train_lang_path):
        train_language(root+p,lang_name[i])