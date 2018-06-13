import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import pylab

G = nx.MultiDiGraph()
#list of kabyle tags
tags=[]
i=0
#extraction du tableau des tags

for ligne in open("c:/tal/tagspos.txt",encoding='utf-8'):
     a=ligne.replace('\n',"")
     if (i!=0):
      b=(a,0,())
      tags.append(b)
     i=i+1

edges=[]    # Edges list
#this function renders the tag index in the tags kab array
def index_of_tag(tag):
    l=0
    while l< len(tags):
        c= tags[l]
        b=c[0]
        #print (b)
        #print (tag)
        if (tag==b):
            return (l)
        l=l+1






regexp ='[-A-Zḍčǧḥṛṣẓṭţɣɛ« ».,:1-9a-z]+/[A-Z]+' # regular expression to retreive the couple (tagged wor/tag)

text=""
#Construction du texte global
first=0
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    if (first!=0):
     text=text+ligne
    first=1


text=text.replace('\n'," ")
text=text.replace("  "," ")
text=text.replace("   "," ")
text=text.replace("\ufeff","")
a=text.split(" ")
i=0
start=0
b=''
while i<len(a)-1:
    iii=b
    #récupérer la paire mot tag
    b=a[i].split("/")  #split a couple
    #print (b[1])

    try:

     tuplea=tags[index_of_tag(b[1])] #look for the index of the tag
    except:
        print (b,iii,'here',b)
        exit()
    #print (tuple)
    number=tuplea[1]+1#increment the tag count
    tuple_tag=tuplea[2]
    list_a=list(tuple_tag)

    if b[1]=='NMP':
        list_a.append(b[0])
    else:
        list_a.append(b[0].lower())
    #print  (list_a)
    tuple_tag=tuple(list_a)
    tags[index_of_tag(b[1])]=(tuplea[0],number,tuple_tag)# update une tag count
    c=a[i+1].split("/") # this is for the last couple word/tag
    if (len(c)!=2):
        print (b,c,'moins de deux',a[i-1])
        exit()
    if(start==0) and (i==0): # the first start edge : First word in the text or the first edge after a dot
        G.add_edges_from([('Start',b[1])], weight=0)
        edges.append(('Start->'+b[1],1))
        G.add_edges_from([(b[1],c[1])], weight=0) # and create an edge betwen the dot and the previous tags
        edges.append((b[1]+'->'+c[1],1))

        start=1
        #print ('start')
    elif (start==0):
        try:
         G.add_edges_from([('Start',c[1])], weight=0) # edge start -> next word after a dot .
         start=1
         edges.append(('Start->'+c[1],1))
        except:
            print(c,b,iii)
            exit()


    elif (c[1]=='.'):

        G.add_edges_from([(c[1],'Stop')], weight=0) # when a dot is found, create an end
        edges.append((c[1]+'->Stop',1))
        G.add_edges_from([(b[1],c[1])], weight=0) # and create an edge betwen the dot and the previous tags
        edges.append((b[1]+'->'+c[1],1))
        start=0



    else:
        G.add_edges_from([(b[1],c[1])], weight=0) # create and edge between two neighbours
        edges.append((b[1]+'->'+c[1],1))

    i=i+1

# this is for the last tag. We will increment its occurence

try:
 tuplea=tags[index_of_tag(c[1])]
except:
    print (c[1])
    exit()


number=tuplea[1]+1
tuple_tag=tuplea[2]
list_a=list(tuple_tag)
list_a.append(c[0])
tuple_tag=tuple(list_a)
try:
 tags[index_of_tag(c[1])]=(tuplea[0],number,tuple_tag)
except:
    print (c[1])
    exit()

#print (tags)
val_map = {}
values = [val_map.get(node, 0.45) for node in G.nodes()]
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

red_edges = [('Start','NMC'),('NMC','Stop')]
edge_colors = ['black' if not edge in red_edges else 'black' for edge in G.edges()]

pos=nx.spring_layout(G)

options = {
    'node_color': 'blue',
    'node_size': 800,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 13,
}
color_map = []
j=0
for node in G:
    #print (node)

    if str(node) =='Start' or str(node) =='Stop':
        color_map.append('blue')

    elif (len(str(node))>=4):
        color_map.append('olive')
    elif (len(str(node))==3):
        color_map.append('yellow')
    elif (len(str(node))==2):
        color_map.append('purple')
    else:
        color_map.append('red')
    j=j+1
nx.draw(G,pos, node_color = color_map, node_size=1500,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
#nx.draw_networkx_labels()
#networkx.draw_networkx_labels(graph,node_positions,font_size=16)
#nx.coloring.greedy_color(G, strategy='largest_first')
#nx.draw_networkx(G, arrows=True, **options)
#print (words)i
j=0
labels={}
for i in G.nodes:

    labels[i]=i

nx.draw_networkx_labels(G,pos,labels,font_size=16)

pylab.axis('off')
pylab.show()


# calculate the occurences of grammatical classes ant show them on histogram
x = np.arange(len(tags))
valeurs=[]
symbols=[]
i=0
while i< len (tags):
    if (tags[i][1] != 0):
        valeurs.append(tags[i][1])
        symbols.append(tags[i][0])
    i=i+1

x = np.arange(len(valeurs))
plt.bar(x, height= valeurs)
##
plt.xticks(x+.5, symbols);
plt.ylabel('Timeḍriwt/Tiseqqaṛ')
plt.xlabel('Ismilen inejrumen')
plt.show()


#calculate probabilities

edges_probabilities=[]

edges_probabilities=[[x,edges.count(x)] for x in set(edges)]





for i in edges_probabilities:
    edges_probabilities[edges_probabilities.index(i)]=(i[0],i[1]/len(edges))
    #print(i[0][0],'+',i[1])



x = np.arange(len(tags))
valeurs=[]
symbols=[]
i=0
while i< len (edges_probabilities):
    if (edges_probabilities[i][1] != 0):
        valeurs.append(edges_probabilities[i][1]*100)
        symbols.append(edges_probabilities[i][0][0])

    i=i+1

x = np.arange(len(valeurs))
plt.bar(x, height= valeurs)
plt.xticks(x+.1, symbols);
plt.ylabel('Probabilité')
plt.xlabel('Transitions')
plt.show()
#print ('yes')

#calcul de la matrice de probabilité



probablilities = []
line=[]
l=0
for i in tags:
    k=0
    line=[]
    for j in tags:
        line.append(0)
        k=k+1
    probablilities.append(line)
    l=l+1

x=0
for j in edges_probabilities:
            x=a
            a=j[0][0].split("->")
            #print (j,'-> ',index_of_tag(a[0]))# print (j[1])
            try:
             probablilities[index_of_tag(a[0])][index_of_tag(a[1])]=j[1]
            except:
                print (x,a,a[0],'->',a[1],j[1])
                exit()

for i in probablilities:
    k=0
    x=0
    for j in i:
        x=j+x

        #print (x)


#######begin cloud
tags1=[]
i=0
for ligne in open("c:/tal/tagspos.txt",encoding='utf-8'):
     a=ligne.replace('\n',"")
     if (i!=0):
      tags1.append(a)
     i=i+1
x=[]
y=[]
for i in tags1:
    x.append(0)
    y.append(0)
#this function renders the tag index in the tags kab array
def index_of_tag1(tag,tags1):
    l=0
    while l< len(tags1):
        c= tags1[l]
        if (tag==c):
            return (l)
        l=l+1
    return tag

for i in edges_probabilities:
    h=i[0][0]
    j=h.split('->')
    x[index_of_tag1(j[0],tags1)]=x[index_of_tag1(j[0],tags1)]+1
    y[index_of_tag1(j[1],tags1)]=y[index_of_tag1(j[1],tags1)]+1
plt1.scatter(x,y,s=10)

plt1.title('Asigna n waggazen : ismilen n tjerrumt')
plt1.xlabel('x')
plt1.ylabel('y')

plt1.show()

x1=[]
y1=[]
for i in edges_probabilities:
    h=i[0]
    j=h[0].split('->')
##    print(j)
    x1.append(x[index_of_tag1(j[0],tags1)]*10000)
    y1.append(x[index_of_tag1(j[1],tags1)]*10000)

plt1.scatter(x1,y1,s=5)

plt1.title('Asigna n waggazen : Tiyugiwin n yismilen n tjerrumt')
plt1.xlabel('x')
plt1.ylabel('y')

plt1.show()

x1=[]
y1=[]
for i in edges_probabilities:
    h=i[0]
    j=h[0].split('->')
##    print(j)
    x1.append(x[index_of_tag1(j[0],tags1)]*10000)
    y1.append(y[index_of_tag1(j[1],tags1)]*10000)

plt1.scatter(x1,y1,s=5)

plt1.title('Asigna n waggazen : Tiyugiwin n yismilen n tjerrumt')
plt1.xlabel('x')
plt1.ylabel('y')

plt1.show()

x1=[]
y1=[]
for i in edges_probabilities:
    h=i[0]
    j=h[0].split('->')
##    print(j)
    x1.append(y[index_of_tag1(j[0],tags1)]*10000)
    y1.append(x[index_of_tag1(j[1],tags1)]*10000)

plt1.scatter(x1,y1,s=5)

plt1.title('Asigna n waggazen : Tiyugiwin n yismilen n tjerrumt')
plt1.xlabel('x')
plt1.ylabel('y')

plt1.show()

x1=[]
y1=[]
for i in edges_probabilities:
    h=i[0]
    j=h[0].split('->')
##    print(j)
    x1.append(y[index_of_tag1(j[0],tags1)]*10000)
    y1.append(y[index_of_tag1(j[1],tags1)]*10000)

plt1.scatter(x1,y1,s=5)

plt1.title('Asigna n waggazen : Tiyugiwin n yismilen n tjerrumt')
plt1.xlabel('x')
plt1.ylabel('y')

plt1.show()

x1=[]
y1=[]
for i in edges_probabilities:
    h=i[0]
    print(i[1])
    j=h[0].split('->')
##    print(j)
    x1.append(y[index_of_tag1(j[0],tags1)]*10000)
    y1.append(i[1]*10000)

plt1.scatter(x1,y1,s=5)

plt1.title('Asigna n waggazen : Tiyugiwin n yismilen n tjerrumt')
plt1.xlabel('x')
plt1.ylabel('y')

plt1.show()
