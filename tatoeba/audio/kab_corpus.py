#avant de procéder, il faut télécharger le corpus texte tatoeba et dézipper le.
f= open("sentences.csv",encoding='utf-8') # corpus dézipé
kab=open("sentences_kab.csv","w+",encoding='utf-8') # le fichier contenant que les phrases kabyles avec identifiant

i=0
line=""
for line in f:
        line=line.replace("\ufeff","")
        values = line.split("\t")

        if (values[1]=="kab"):
         kab.write(line)


f.close()
kab.close()
