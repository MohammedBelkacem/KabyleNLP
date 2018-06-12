tirgalin=['a','e','i','u']
tighra=['ɛ','b','c','č','d','ḍ','f','g','ɣ','ǧ','h','ḥ','j','k','l','m','n','p','q','r','ṛ','s','ṣ','t','ṭ','v','w','x','y','z','ẓ','ţ']
syllabe=['v','vc','vcc','cv','cvc','cvcc','ccv','ccvc','ccvcc']
assimilations=[('dt','ţ'),('ny','gg')]
#for taghret in tighra:
#    print taghret.decode('utf8')
def sekyed (azrir):
    a=""
    for i in azrir:
        if i in tighra:
            a=a+'c'
        else:
            a=a+'v'
    return a

text= "Azul meṛṛa fell-awen ay imdukal d timdukal"
text=text.replace('-',' ')
text=text.replace(',',' ')
text=text.replace('.',' ')
text=text.replace(' d ',' ed ')
text=text.lower()
text=text
i=0
for awal in text.split():
 #print (awal)
 while (len(awal)>0):

  if (i!=0):
    exit
  i=1

  if len(awal)>=5 and sekyed (awal[0:5]) in syllabe:
        print (awal[0:5],"->",sekyed (awal[0:5]))
        awal=awal[5:len(awal)]
        i=0

  elif len(awal)>=4 and sekyed (awal[0:4]) in syllabe:
            print (awal[0:4],"->",sekyed (awal[0:4]))
            awal=awal[4:len(awal)]
            i=0
  elif len(awal)>=3 and sekyed (awal[0:3]) in syllabe:
                print (awal[0:3],"->",sekyed (awal[0:3]))
                awal=awal[3:len(awal)]
                i=0
  elif len(awal)>=2 and sekyed (awal[0:2]) in syllabe:
                    print (awal[0:2],"->",sekyed (awal[0:2]))
                    awal=awal[2:len(awal)]
                    i=0
  elif len(awal)>=1 and sekyed (awal[0:1]) in syllabe:
                        print (awal[0:1],"->",sekyed (awal[0:1]))
                        awal=awal[1:len(awal)]
                        i=0
