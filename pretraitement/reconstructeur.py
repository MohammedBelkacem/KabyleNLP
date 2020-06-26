#-------------------------------------------------------------------------------
# Name:        Postagginf or kabyle
# Purpose:     POS TAG for Kabyle
#
# Author:      Muḥend Belqasem
#
# Created:     15/01/2019
# Copyright:   (c) Belkacem Mohammed 2019
# Licence:     <MIT>
from sklearn_crfsuite import CRF

def features(sentence, index):
    return {
        'word': sentence[index], #awal s timmad-is
        'is_one_letter': len(sentence[index])== 1, # me yegber kan yiwen n usekkil
        #'maybe_annexed':maybe_annexed(sentence[index])==True,
        'is_first': index == 0, # ma yezga-d dege tazwara n tefyirt
        'is_last': index == len(sentence) - 1, # yezga-d deg taggar n tefyirt
        'is_capitalized': sentence[index][0].upper() == sentence[index][0], # ma yettwaru s usekkel ameqqran deg tazwara
        'is_all_caps': sentence[index].upper() == sentence[index], # ma yettwaru meṛṛa s usekkil ameqqran
        'is_all_lower': sentence[index].lower() == sentence[index], # ma yettwaru meṛṛa s usekkil meẓẓiyen
        'prefix-1': sentence[index][0],   #asekkil amenzu seg wawal
        'prefix-2': sentence[index][:2], # sin isekkilen imenza seg wawal
        'prefix-3': sentence[index][:3], # 3 isekkilen imenza seg wawal
        'prefix-4': sentence[index][:4], # 4 isekkilen imenza seg wawal
        'prefix-5': sentence[index][:5], # 5 isekkilen uzwiren tettecmumuḥenḍ (aoriste intensif)
        'suffix-1': sentence[index][-1], # asekkil aneggaru seg wawal
        'suffix-2': sentence[index][-2:], # 2 isekkilen ineggura seg wawal
        'suffix-3': sentence[index][-3:], # 3 isekkilen ineggura seg wawal
        'suffix-4': sentence[index][-4:], # 4 isekkilen ineggura seg wawal
        'prev_word': '' if index == 0 else sentence[index - 1], # awal uzwir
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1], # awal uḍfir
        'is_numeric': sentence[index].isdigit(), # ma yettwaru kan s yizwilen
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:] # ma yegber asekkil ameqqran deg tlemmast
    }



model = CRF()


def pos_tag(sentence,model):
    try:
     sentence_features = [features(sentence, index) for index in range(len(sentence))]
    except:
        return (sentence)
    return list(zip(sentence, model.predict([sentence_features])[0]))


from joblib import dump, load
clf = load('modelap.joblib')

Sentence ="awi ten id".strip()
izirig=""
xx=pos_tag(Sentence.split(" "),clf)
for u in xx:
        try:
         yy=u[0]+'/'+u[1]
         izirig=izirig+yy+" "
        except:
            print (Sentence+"ERROR IN SENTENCE")

            exit()

line=izirig.strip().replace("\ufeff","").replace("\n","").split(" ")

final_sentence=""
for i in line:
        j=i.split("/")
        try:
         if j[1]=="NOP":
            final_sentence=final_sentence+" "+j[0]
         else:
            final_sentence=final_sentence+" "+j[1].replace("gh","ɣ").replace("dh","ḍ")
        except:
            print(line)
            exit()
final_sentence=final_sentence.replace(" -",'-').replace("- ","-").strip()
print (final_sentence)
