import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
taille=0
first=0
word_all=[]
words_diffrent=[]
total=0
tags=[]
i=0
Ponctuation=['...',',',';','?','!',':','"','(',')','*','_','.','[',']','{','}','«','»','+','=','.','$','“','”','-']

#extraction du tableau des tags
for ligne in open("c:/tal/tagspos.txt",encoding='utf-8'):
     a=ligne.replace('\n',"")
     if (i!=0):
      b=(a,0)
      tags.append(b)
     i=i+1
def index_of_tag(tag,tags):
    l=0
    while l< len(tags):
        c= tags[l]
        b=c[0]
        #print (b)
        #print (tag)
        if (tag==b):
            return (l)
        l=l+1
b=""
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    if (first!=0):

     #ligne=ligne.lower()
     first=1
     ligne=ligne.replace("\n","")
     a=ligne.split(" ")

     for i in a:
        h=b
        b=i.split("/")
        total=total+1
        if True:
            taille=taille+1
            if(b[1]=='NMP'):
             word_all.append(b[0])
            else:
             word_all.append(b[0].lower())
        kk=index_of_tag(b[1],tags)
        try:

         d=tags[kk]
        except:
            print(b[1])
            print(tags,'voir ici',d,kk,h)
            exit()
        z=d[1]
        c=(tags[kk][0],z+1)
        #print (c)
        tags[kk]=c


    else:
        first=1
#print(taille,'',len(word_all))
for i in word_all:
    if i in words_diffrent:
        d=0
    else:
        words_diffrent.append(i)
#print(words_diffrent)
print(total,'->',len(word_all),'->',len(words_diffrent))

# calcul du pourcentage d'apparition des de certaines classes
valeurs=[]
symbols=[]
i=0

while i< len (tags):
    if (tags[i][1] != 0 and tags[i][0] not in Ponctuation ):
        valeurs.append(tags[i][1])
        symbols.append(tags[i][0])

    i=i+1

labels=[]
fracs=[]
for i in tags:
    #print (i[1])
    if (i [1] >= 40):
     labels.append(i[0])
     fracs.append(i[1])

##explode = (0, 0, 0, 0)
##
### Make square figures and axes
##
##
### Turn off shadow for tiny plot with exploded slice.
##

patches, texts, autotexts = plt.pie(fracs,
                                    labels=labels, autopct='%.0f%%',
                                    shadow=False, radius=1)
for t in texts:
    t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Ifmiḍen n yismilen inejrumanen')

##
plt.show()

##calcul du pourcentage de la ponctuation par rapport aux mots

labels=['PNCT','ISEKKILEN']
fracs=[]
x=0

#print (tags)
y=0
for i in tags:
    #print (i[0])
    if (i[0]  in Ponctuation):
        #print ("yes")
        x=x+i[1]
    else:
     y=y+i[1]
fracs=[x,y]
patches, texts, autotexts = plt.pie(fracs,
                                    labels=labels, autopct='%.0f%%',
                                    shadow=False, radius=1)
for t in texts:
    t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Ifmiḍen n yisekkilen  d yizamulen n usenqeḍ di teqbaylit')

plt.show()
### calcul du nombre de mots par taille dans le corpus

taille=[]
u=0
while u<80:
    taille.append(0)
    u=u+1

labels=[]

first=0
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    #print(ligne)
    a=ligne.split()
    #print(a)
    if (first!=0):

        for i in a:
            b=i.split('/')
            if (b[1] not in Ponctuation):
                taille[len(b[0])-1]=taille[len(b[0])-1]+1
    first=1
j=1
tail=[]
for i in taille:
    if i!=0:
        #print(i)
        tail.append(i)
        labels.append(str(j)+" isekkilen")
    j=j+1


patches, texts, autotexts = plt.pie(tail,
                                    labels=labels, autopct='%.0f%%',
                                    shadow=False, radius=1)
for t in texts:
    t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Ifmiḍen n teɣzi n wawalen deg uḍris n ulmud')

plt.show()

#longueur des phrases

taille=[]
i=0
while  i<=80:
    taille.append(0)
    i=i+1
labels=[]

first=0
nb=0
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    #print(ligne)
    a=ligne.split()
    #print(a)
    if (first!=0):
        nb=0
        for i in a:
            b=i.split('/')
            if (b[1]  in Ponctuation):
                nb=nb+1
        try:
         taille[len(a)-nb-1]=taille[len(a)-nb-1]+1
        except:
            print (len(a), nb,a,taille,'Erreur')
            exit ()
    first=1
j=1
tail=[]
for i in taille:
    if i!=0:
        #print(i)
        tail.append(i)
        labels.append(str(j)+" n wawalen")
    j=j+1


patches, texts, autotexts = plt.pie(tail,
                                    labels=labels, autopct='%.0f%%',
                                    shadow=False, radius=1)
for t in texts:
    t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Ifmiḍen n teɣzi n tifyar deg uḍris n ulmud')

plt.show()

# calcul de nombre de mots ambigues
first=0
tagpos=[]
words=[]
for ligne in open("c:/tal/tagspos.txt",encoding='utf-8'):
    if (first!=0):
        a=ligne.split()
        tagpos.append(a[0])
    first=1

for i in tagpos:
    words.append([])
first=0
def index_of_tag1(tag,tags):
    l=0
    while l< len(tags):
        c= tags[l]

        #print (c,'hihihihi')
        if (tag==c):
            #print("dddddddddddd",l)
            return (l)
        l=l+1

for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    #print(ligne)
    a=ligne.split()
    #print(a)
    if (first!=0):
        for i in a:
            b=i.split('/')

            indice=index_of_tag1(b[1],tagpos)

            try:
             x=words[indice]
            except:
                print(tagpos,a,b[1])
                exit()
            try:
             x.append(b[0])
            except:
                print   ("fffff",indice,words[indice])
                exit ()
            words[indice]=x
    first=1

Verbs=['VAF',   #aoriste futur
'VAI',    # aoriste impératif
'VAIT',   #aoriste intensif
'VII',   #impératif intensif
'VP',    # prétérit
'VPA',   #participe aoriste
'VPAIN', #participe aoriste intensif négatif
'VPAIP', #participe aoriste intensif positif
'VPN',   # prétérit négatif
'VPPN',  #participe prétérit négatif
'VPPP',  # participe prétérit positif
'VS'     # verbe subjonctif
]
occurences=[]
for i in Verbs:

 print(tagpos[index_of_tag1(i,tagpos)],words[index_of_tag1(i,tagpos)])
 occurences.append(len(words[index_of_tag1(i,tagpos)]))

patches, texts, autotexts = plt.pie(occurences,
                                    labels=Verbs, autopct='%.0f%%',
                                    shadow=False, radius=1)
for t in texts:
    t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Ifmiḍen n yimyagen s tmeẓri(aspect) deg uḍris n ulmud')

plt.show()

i=0

x = np.arange(len(occurences))
plt.bar(x, height= occurences)

plt.xticks(x+.5, Verbs);
plt.ylabel('Timeḍriwt/Tiseqqaṛ')
plt.xlabel('Imyagen')
plt.show()

taille2=[]
i=0
while i<120:
    taille2.append(0)
    i=i+1
x=""
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    #print(ligne)
    a=ligne.split()
    if(len(a)>80):
     for k in a:
        l=k.split('/')
        x=x+' '+l[0]
     print(x)
    #print(a)
    taille2[len(a)]=taille2[len(a)]+1
i=0
for j in taille2:
    if j!=0:
        print (i,'->',j)
    i=i+1
#analyse des mots différents
Ponctuation=['...',',',';','?','!',':','"','(',')','*','_','.','[',']','{','}','«','»','+','=','“','”']
stopwords=[]
#for izirig in open("c:/tal/affixecolles.txt",encoding='utf-8'):


awalen=[]
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    ligne=ligne.replace("\n","")
    ligne=ligne.replace("\ufeff","")
    ligne=ligne.split()
    for i in ligne:
        k=i.split("/")
        if k[0] not in Ponctuation:
         k[0]=k[0].lower()
         awalen.append(k[0])


awalen_yemgaraden=[]
for i in awalen:
    if i not in awalen_yemgaraden:
        awalen_yemgaraden.append(i)

#calcul de l'occurence:
occurences=[]
for i in awalen_yemgaraden:
    b=0
    for j in awalen:
        if i ==j:
            b=b+1


    occurences.append((i,b))
nb=0
for i in occurences:
    b=i[1]
    if b>1:
        nb=nb+1

print(occurences,nb)
print(awalen_yemgaraden,len(awalen_yemgaraden))

Types=['Tikelt', 'Ugar n tikelt']
Types1=[len(awalen_yemgaraden)-nb,nb]
patches, texts, autotexts = plt.pie(Types1,
                                    labels=Types, autopct='%.0f%%',
                                    shadow=False, radius=1)
for t in texts:
    t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Tasleḍt n uḍris n ulmad: afmiḍi n wawalen i d-yettuɣalen ugar n tikelt')

plt.show()

