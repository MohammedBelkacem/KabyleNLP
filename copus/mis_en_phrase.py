#Ce texte permet  de générer un texte normalisé d'une phrase par ligne dans le fichier cible

f= open("c:/tal/original_text.txt",encoding='utf-8')
g=open("c:/tal/brut_text.txt","w+",encoding='utf-8')



for line in f:
    line=line.replace("\ufeff","")
    x=line
    i=0
    while (x!=""):

        phrase=x[0:x.find('.')+1]

        x=x[x.find('.')+2:len(x)]
        #print(x)
        phrase=phrase+'\n'
        g.write(phrase)


f.close()
g.close()
