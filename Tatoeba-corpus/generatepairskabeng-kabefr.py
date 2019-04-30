linkskabfr=open("c:/tal/tatoeba/links/linksfr.csv",encoding='utf-8')


numbers=[]
numbers2=[]
for line in linkskabfr:
        line1=line.replace("\ufeff","")
        line1=line1.strip()
        values = line1.split("\t")
        numbers.append(values)
linkskabfr.close()

linkskaben=open("c:/tal/tatoeba/links/linksen.csv",encoding='utf-8')

for line in linkskaben:
        line1=line.replace("\ufeff","")
        line1=line1.strip()
        values = line1.split("\t")
        numbers2.append(values)
linkskaben.close()
