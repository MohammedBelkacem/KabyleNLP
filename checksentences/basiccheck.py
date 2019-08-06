
minuscule=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','č','ḍ','ǧ','ḥ','ɣ','ṛ','ṣ','ṭ','ɛ','ẓ']

ponctuation=['.','?',':',',','-','!','\n',' ']

majuscule=[]
for i  in minuscule:
      majuscule.append(i.upper())

def checkSentence (sentence):

    for i in sentence:
        if i  not in minuscule and  i  not in majuscule and i not in ponctuation:
               return False
    return True

f= open("sentenceskab.csv",encoding='utf-8')

err=open("errors.csv","w+",encoding='utf-8')
corr=open("correct.csv","w+",encoding='utf-8')


i=0
line=""
for line in f:
        line=line.replace("\ufeff","")
        if checkSentence(line):
            corr.write(line)
        else:
            err.write(line)



f.close()
err.close()
corr.close()
