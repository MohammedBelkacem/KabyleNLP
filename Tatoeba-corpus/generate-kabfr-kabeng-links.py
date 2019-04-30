kabfr=open("sentences_kab_fra.csv",encoding='utf-8')

numbers=[]
numbers2=[]
for line in kabfr:
        line=line.replace("\ufeff","")
        values = line.split("\t")
        numbers.append(values[0])
kabfr.close()

kaben=open("sentences_kab_eng.csv",encoding='utf-8')

for line in kaben:
        line=line.replace("\ufeff","")
        values = line.split("\t")
        numbers2.append(values[0])
        
kaben.close()



links=open("links.csv",encoding='utf-8')
linkskabfr=open("linksfr.csv","w+",encoding='utf-8')
linkskaben=open("linksen.csv","w+",encoding='utf-8')
for line in links:
        line1=line.replace("\ufeff","")
        line1=line1.strip()
        values = line1.split("\t")
        if values[0] in numbers or values[1] in numbers:
             linkskabfr.write(line)
        if values[0] in numbers2 or values[1] in numbers2:
             linkskaben.write(line)
links.close()
linkskabfr.close()
linkskaben.close()
