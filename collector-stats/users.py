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
