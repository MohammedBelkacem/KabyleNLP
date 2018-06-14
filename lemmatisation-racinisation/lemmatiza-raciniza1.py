#-------------------------------------------------------------------------------
# Name:        lemmatize aoriste futur
# Purpose:     Lemmatization for Kabyle
#
# Author:      Muḥend Belqasem
#
# Created:     15/01/2018
# Copyright:   (c) Belkacem Mohammed 2018
# Licence:     <MIT>
#-------------------------------------------------------------------------------
def sekyed_asekkil (asekkil,tighra):
    #yella=False
    for i in tighra:
        if asekkil==i:
            return True

    return False

def amasal (azrir):
    amasal=''
    for i in azrir:
        if i =='e':
            amasal=amasal+'e'
        else:
            amasal = amasal+'c'
    return amasal


voyelles=['a','e','i','u']
imasalen=[{'cecec',0}]# ajouter ici les formes issues des différentes flexions après avoir former le radical sans suppression de la lettre e issue de la flexion verbiale
for line in open("C:/tal/corpus-aoriste2.txt",encoding='utf-8'):
    #Aoriste 1 ière personne
        i = line.split()
        i= i[0]
        a=""
        #print i

        if (i.endswith('iḍ') or i.endswith('uḍ') ) and ((i.startswith('ta') or i.startswith('te'))):
            if (i.startswith('ta')):
             a=i[1:len(i)-1]

            else:
                if i.startswith('te'):
                    a=i[2:len(i)-1]



            #print i.decode('utf8')
        else:
            if (i.endswith('iḍ')) and (i.startswith('t')):
                        a=i[1:len(i)-1]

            if (i.endswith('eḍ')) and (i.startswith('te')  ):
             a=i[1:len(i)-1]
            if i.endswith('eḍ') and i.startswith('t') and not i.startswith('te')  :
             a=i[1:len(i)-1]

             #print a
            if i.startswith('ta') or i.startswith('te'):
             if i.startswith('ta'):
                  a=i[1:len(i)-1]
             if i.startswith('te'):
                a=i[2:len(i)-1]


             if (len(a)>=3 and a[len(a)-1] not in voyelles): # Si l'avant dernière lettre n'est pas une voyelle
                if (a[len(a)-2]!=a[len(a)-1]): #Si les deux dernière lettre ne sont pas les même
                 #print a[0:len(a)-1], a[len(a)-2], a[len(a)-1]
                 a=a[0:len(a)-1]+'e'+a[len(a)-1] # on insère alors un e
                 #print a , 'ici'
                else:
                    if (len (a)<=2 and a[len(a)-1] not in voyelles):
                          a='e'+a[len(a)-2:len(a)] # si plus de deux consonnes
                          #print a,'ici'

            if (len (a)<=2 ):

                          #print a,'ici',len(a),a[len(a)-2:len(a)-1]
                          a='e'+a[len(a)-2:len(a)] # si plus de deux consonnes
                          #print a,'ici', a[len(a)-1]


        # traietement des cas de déplacement de e
        if (amasal(a)=='cecec') :
            a=a[0]+a[2:len(a)]
        if (amasal(a)=='ccccecec'):
            a=a[0:4]+a[5:len(a)]
        if (amasal(a)=='cccecec'):
            a=a[0:3]+a[4:len(a)]
        if (amasal(a)=='ccecec'):
            a=a[0:1]+'e'+a[1:2]+a[len(a)-3:len(a)]
        if (amasal(a)=='ccececec'):
            #print a
            a=a[0:4]+a[len(a)-3:len(a)]


        print (i, '->', a)
        a=""
