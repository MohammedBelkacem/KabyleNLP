import json
i= 0
creators=[]
validators=[]
with open('sentences.json',encoding='utf-8') as json_file:
    data = json.load(json_file)
    for p in data:

            #print(a)
        if p['username'] not in creators:
                creators.append(p['username'])
        for i in p['valid']:
            if i not in validators:
                validators.append(i)


print ("creators")

for c in creators: print( c)
print ("validators")
for c in validators: print( c)
countcreators=[]
countvalidators=[]

for k in creators:
    h=(k,0)
    countcreators.append(h)

for k in validators:
    h=(k,0)
    countvalidators.append(h)

with open('sentences.json',encoding='utf-8') as json_file:
    data = json.load(json_file)
    for p in data:

            #print(a)
        if p['username']  in creators:
                countcreators[creators.index(p['username'])]=(countcreators[creators.index(p['username'])][0],countcreators[creators.index(p['username'])][1]+1)
                #creators.append(p['username'])
        for i in p['valid']:
            if i  in validators:

                countvalidators[validators.index(i)]=(countvalidators[validators.index(i)][0],countvalidators[validators.index(i)][1]+1)


print (countvalidators)

print (countcreators)
