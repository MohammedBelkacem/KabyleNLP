from sklearn_crfsuite import CRF
from nltk.tag.util import untag
from sklearn_crfsuite import metrics

tagged_sentences=[]
#Construction du texte global à aprtir du corpus étiqueté
first=0
taille2=0
for ligne in open("c:/tal/corpus-kab.txt",encoding='utf-8'):
    taille=0
    if (first!=0):
        sentence=[]
        line=ligne.split()
        taille=len(line)
        for i in line:
            j=i.split('/')
            couple=(j[0],j[1])
            sentence.append(couple)
        taille2=taille+taille2
        tagged_sentences.append(sentence)
    first=1

print("Amḍan n tefyar: ", len(tagged_sentences))
print("Amḍan n yiferdisen: ", taille2)

#Définition des caractériqtuques d'un mot
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

#transformation du corpus x: contient les tokens et y les tags
def transform_to_dataset(tagged_sentences):
    X, y = [], []

    for tagged in tagged_sentences:
        X.append([features(untag(tagged), index) for index in range(len(tagged))])
        y.append([tag for _, tag in tagged])

    return X, y
print(len(tagged_sentences))
total=int(len(tagged_sentences)*0.80)
print(total)
#train=tagged_sentences

X1_train, y1_train = transform_to_dataset(tagged_sentences[:total])
print(len(tagged_sentences[:total]))
print(len(tagged_sentences[total:]))

X_test, y_test = transform_to_dataset(tagged_sentences[total:])
#déclaration du modèle suivant l'algotihme  lbfgs
model = CRF(
    algorithm='pa', # Passive Aggressive (PA).
                       #Used to pos tag words or other information provided by the model within the situation.



    max_iterations=100,
    all_possible_transitions=True
)
#entrainement
model.fit(X1_train, y1_train)

y_pred = model.predict(X_test)
labels = list(model.classes_)
print(labels)
metrics.flat_f1_score(y_test, y_pred,
                      average='weighted', labels=labels)
print (model.score(X1_train, y1_train))
# Sauvegarde du modèle

#from joblib import dump, load
#dump(model, 'model.joblib')
