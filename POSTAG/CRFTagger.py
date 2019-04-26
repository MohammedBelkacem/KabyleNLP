from sklearn_crfsuite import CRF
aḍris=[]
amenzu=0
uḍfiren=[]
uzwiren=[]
Asenqeḍ=['...',',',';','?','!',':','"','(',')','*','_','.','[',']','{','}','«','»','+','=','“','”']
for i in open("c:/tal/affixescolles.txt",encoding='utf-8'):
    a=i
    a=a.replace("\ufeff","")
    a=a.replace("\n","")
    if (a[len(a)-1]=="-"):

     uzwiren.append(str(a))
    else:
       uḍfiren.append(str(a))

def tokenize_awal(awal,uḍfiren,uzwiren):
    a=''
    amurfim=awal[0:awal.find('-')+1]

    awal_yebḍan=''
    if (amurfim in uzwiren):
        awal=awal[awal.find('-')+1:len(awal)]
        awal_yebḍan=awal_yebḍan+' '+amurfim
        while awal.find('-')>=0:

            amurfim=awal[0:awal.find('-')+1]
            awal=awal[awal.find('-')+1:len(awal)]
            awal_yebḍan=awal_yebḍan+' '+amurfim
        awal_yebḍan=awal_yebḍan+' '+awal
    else:
        amurfim=awal[0:awal.find('-')]
        awal_yebḍan=awal_yebḍan+' '+amurfim
        awal=awal[awal.find('-')+1:len(awal)]
        while awal.find('-')>=0:

           amurfim=awal[0:awal.find('-')]
           awal_yebḍan=awal_yebḍan+' '+'-'+amurfim
           awal=awal[awal.find('-')+1:len(awal)]
    if ('-'+awal in uḍfiren):
         awal_yebḍan=awal_yebḍan+' '+'-'+awal
    else:
         awal_yebḍan=awal_yebḍan



    return awal_yebḍan

def tokenize(sentence,uḍfiren,uzwiren):
       a=sentence.split()
       tafyirt1=""
       for i in a: #mots
        if(i.find('-')<0):
            tafyirt1=tafyirt1+' '+i
        else:
            awals=tokenize_awal(i,uḍfiren,uzwiren)
            tafyirt1=tafyirt1+' '+awals
       tafyirt1=tafyirt1.strip()
       return tafyirt1
def maybe_annexed(w):
   morphems=['u','we','yi','ye','wa','wu','ti','te','t']
   consons=['b','c','č','d','ḍ','f','g','ǧ','h','ḥ','j','k','l','m','n','p','q','ɣ','r','ṛ','s','ṣ','t','ṭ','v','w','ɛ','x','y','z','ẓ']
   if len(w)>=3:
    a=w[0:2]
    if a in morphems:
        return True
    else:
        a=w[0]
        if a == 't' and w[1] in consons:
            return True;
        else:
            if a in morphems:
                return True;
            else:
                return False;

   else:
    return False;


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
#dump(model, 'lodel.joblib')
#print(metrics.flat_accuracy_score(y_test, y_pred))
clf = load('c:/tal/kab-POS-tagl.joblib')

f= open("tokenized_text.txt","w+",encoding='utf-8')
h= open("tagged_text.txt","w+",encoding='utf-8')
g=open("brut_text.txt",encoding='utf-8')
for adur in g:
    #print (adur)
    for i in Asenqeḍ:

        if i=='.':
            adur=adur.replace(i,' '+i+' ')
        else:
            adur=adur.replace(i,' '+i+' ')
    adur=adur.replace("\ufeff","")

    ligne=tokenize(adur,uḍfiren,uzwiren)

    ligne=ligne.replace("  "," ")
    ligne=ligne
    izirig=""
    izirig1=ligne

    f.write(izirig1+'\n')
    #print (izirig1.split(" "))
    xx=pos_tag(izirig1.split(" "),clf)
    for u in xx:
        try:
         yy=u[0]+'/'+u[1]
         izirig=izirig+yy+" "
        except:
            print (izirig1+"$$$$$")
            f.close()
            g.close()
            h.close()
            exit()

    #print(xx)
    h.write(izirig+'\n')

    #t.sleep(0.5)
    #print ("tafyirt: ",ligne, "beṭṭu: ",izirig1, "acraḍ :",izirig)

f.close()
g.close()
h.close()