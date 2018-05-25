#cet algorithme permet d'analyser le corpus pour d'éventuelle érreurs,
#lors des tests sur des textes, le tagger va tager anormalement, le résulat vous permettra de localiser l'erreur  sur le corpus
amenzu=0

for izirig in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    go=0
    if (amenzu!=0):

     #ligne=ligne.lower()
     amenzu=1
     izirig=izirig.replace("\n","")
     a=izirig.split(" ")

     for i in a:

        b=i.split("/")
        if go==1:
            if (precedent[1]=='NCM') and (b[1]=='VAF'):
                print(precedent,'---->',b,a)

                #exit()

        precedent=b
        go=1
        try:
         if (b[1]!='NMP'):
            b[0]=b[0].lower()
         else:
            b[0]=b[0].lower()
        except:
            print(b,'erreur')
            exit()


    else:
        amenzu=1
