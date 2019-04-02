from sklearn_crfsuite import CRF
from nltk.tag.util import untag
from sklearn_crfsuite import metrics

tagged_sentences=[]
#Construction du texte global
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

def features(sentence, index):
    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }


cutoff = int(.75 * len(tagged_sentences))
training_sentences = tagged_sentences[:cutoff]
test_sentences = tagged_sentences[cutoff:]
def transform_to_dataset(tagged_sentences):
    X, y = [], []

    for tagged in tagged_sentences:
        X.append([features(untag(tagged), index) for index in range(len(tagged))])
        y.append([tag for _, tag in tagged])

    return X, y

X_train, y_train = transform_to_dataset(training_sentences)
X_test, y_test = transform_to_dataset(test_sentences)


model = CRF()
model.fit(X_train, y_train)
sentences = [['Nekk', 'd', 'amjaḥ','!'],['wali','iman','-ik','ɣer','lemri','.'],['bɣiɣ','ad','as-','ten-','id-','awiɣ','i','baba','-s','azekka','.']]

def pos_tag(sentence):
    sentence_features = [features(sentence, index) for index in range(len(sentence))]
    return list(zip(sentence, model.predict([sentence_features])[0]))

print ("ASEKYED")
for sentence in sentences:
    print(pos_tag(sentence))


y_pred = model.predict(X_test)
print(metrics.flat_accuracy_score(y_test, y_pred))
