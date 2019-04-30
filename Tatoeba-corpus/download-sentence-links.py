
import wget

files=[
'http://downloads.tatoeba.org/exports/sentences.tar.bz2',
'http://downloads.tatoeba.org/exports/links.tar.bz2',

]
i=1
for url in files:

 wget.download(url)
 i=i+1
