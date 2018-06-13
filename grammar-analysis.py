import nltk
groucho_grammar = nltk.CFG.fromstring("""
Tafyirt -> GV COD COI | GV GN | GV COD | GV COI | AsemmImez Aseɣru
AsemmadImez -> TazTil Isem
Aseɣru -> Isem Udfir
TazTim -> D
Isem -> azefzaw | urgaz
Uḍfir -> '-a'
GV ->VB | VB PRP
COD ->NM
COI -> PRP NM
GN -> NM ADJ
ADJ -> PRP NM
VB ->'walaɣ'
PRP -> 's'
NM ->'argaz' | 'nwaḍer'
 """)


print (groucho_grammar)

tafyrit=""
sent = ['walaɣ','argaz','s','nwaḍer']
for i in sent :
    tafyrit= tafyrit+" "+ i

parser = nltk.ChartParser(groucho_grammar)
print (parser)
print ('tafyirt: ', tafyrit)
print ('tasleḍt:')

for tree in parser.parse(sent):
    print(tree)
