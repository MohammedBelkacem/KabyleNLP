#Ce script télécharge les phrases et leur audio de langue kabyle à partir de Tatoeba.
#il créera un dosssier par page et dans chaque dossier 100 fichiers audio et un fichier texte
#qui contient toutes les phrases de la page en question et qui  aux audio téléchargés dans le même dossier.
import re
import os
import wget
MaxPage=281 # mettre ici le numéro de la dernière page du corpus vocal Kabyle - visible à droite sur Tatoeba, 281 jusqu'à présent

url1 = "https://tatoeba.org/kab/audio/index/kab"
##
i=0

while i<=MaxPage:
 dir="tatoe"+str(i)
 os.mkdir(dir,777)
 html="tatoe"+str(i)+"/tatoe"+str(i)+".html"

 if i!=0:
    extention="?page="+str(i)

 else:
    extention=""

 url= url1+extention
 wget.download(url, html)
 g=open(html,encoding='utf-8')
 text="tatoe"+str(i)+"/tatoe"+str(i)+".txt"
 h=open(text,'w+',encoding='utf-8')

 files=[]
 for line in g:
  searchObj = re.search( r'.mp3', line, re.M|re.I)
  if searchObj:
    text=line.split("<")[23].split(">")[1]
    h.write(text+'\n'+"\n")
    audio=line.split("<")[28].split(" ")[1].replace('href=',"").replace('"',"").replace("\n","")
    audio1=audio.replace("https://audio.tatoeba.org/sentences/kab/","")
    audio1="tatoe"+str(i)+"/"+audio1
    wget.download(audio,audio1)
 g.close()
 h.close()
 i=i+1
 os.remove(html)
