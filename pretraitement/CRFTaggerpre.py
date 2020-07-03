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
        'word': sentence[index],    # Awal s timmad-is
        'is_first': index == 0,     # Ma yezga-d deg tazwar n tefyirt
        'is_last': index == len(sentence) - 1, # Ma yezgma-d deg taggar n tefyirt
        'is_capitalized': sentence[index][0].upper() == sentence[index][0], # MA ibeddu s usekkil meqqren
        'is_all_caps': sentence[index].upper() == sentence[index], # Ma yura meṛṛa s usekkil meqqren
        'is_all_lower': sentence[index].lower() == sentence[index], # ma yura meṛṛa s usekkil meẓẓiyen
        'prefix-1': sentence[index][0], #1 usekkil uzwir
        'prefix-2': sentence[index][:2], #2 isekkilen uzwiren
        'prefix-3': sentence[index][:3], #3 isekkilen uzwiren
        'prefix-4': sentence[index][:4], # 4 isekkilen uzwiren
        'prefix-5': sentence[index][:5], # 4 isekkilen uzwiren tettecmumuḥenḍ (aoriste intensif)
        'suffix-1': sentence[index][-1], #1 usekkil uḍfir
        'suffix-2': sentence[index][-2:], #2 isekkilen uḍfiren
        'suffix-3': sentence[index][-3:], #3 isekkilen uḍfiren
        'suffix-4': sentence[index][-4:], #2 isekkilen uḍfiren
        'prev_word': '' if index == 0 else sentence[index - 1], #awal uzwir
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1], #awal uḍfir

        'is_numeric': sentence[index].isdigit(),  #ma yegber kan izwilen
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:] #ma yegber asekkil meqqren daxel-is

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

Sentence ="axxam inna nkent d ameqqṛan".strip()
izirig=""
xx=pos_tag(Sentence.split(" "),clf)

print(xx)
for u in xx:
        try:
         yy=u[0]+'/'+u[1]
         izirig=izirig+yy+" "
        except:
            print (Sentence+"ERROR IN SENTENCE")

            exit()

line=izirig.strip().replace("\ufeff","").replace("\n","").split(" ")
suffixe=['PSV','PDS','PAP','PAN', 'PADV', 'PAD', 'PAINT', 'PAPR']
prefixe=['PPV','PDP']

final_sentence=""
for i in line:
        j=i.split("/")
        try:
         if '-' not in j[1]:
            final_sentence=final_sentence+" "+j[0]
         else:
            final_sentence=final_sentence+" "+j[1].replace("gh","ɣ").replace("dh","ḍ")
        except:
            print(line)
            exit()
final_sentence=final_sentence.replace(" -",'-').replace("- ","-").strip()
print (final_sentence)