f= open("c:/tal/tatoeba/sentences/sentences.csv",encoding='utf-8')
kabfr=open("c:/tal/tatoeba/sentences/sentences_kab_fra.csv","w+",encoding='utf-8')
kaben=open("c:/tal/tatoeba/sentences/sentences_kab_eng.csv","w+",encoding='utf-8')
i=0
line=""
for line in f:
        line=line.replace("\ufeff","")
        #values = line.strip()
        values = line.split("\t")

        #print(values[1])
        if (values[1]=="fra") or (values[1]=="kab"):
         kabfr.write(line)
        if (values[1]=="eng") or (values[1]=="kab"):
         kaben.write(line)
         #print(line[12:])
         #i=i+1


##        if i>12:
##            exit()




f.close()
kaben.close()
kabfr.close()
