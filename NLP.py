from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet
import os
import json
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from fuzzywuzzy import fuzz
from pathlib import Path

check=json.loads(open("news.json").read())
output=[]
flag=0
for q in check:
    flag=0
    for j in word_tokenize(str(q['All_text'])):
        if j=='Petroleum' or j=='petroleum' or j=='off-shore' or j=='Off-shore' or j=='Offshore' or j=='offshore' or j=='refining' or j=='crude oil' or j=='petrochemical products' or j=='LNG' or j=='gas processing' or j=='pipeline transportation' or j=='delayed cracker' or j=='cocker' or j=='petrochemical energy'or j=='petrol' or j=='diesel' or j=='LPG' or j=='Gas processing' or j=='Pipeline transportation' or j=='Delayed cracker' or j=='Cocker' or j=='Petrochemical energy'or j=='Petrol' or j=='Diesel':
            flag=1
            break
    if flag==1:
        output.append({'url':q['url'],'All_text' :q['All_text']})

output1=[]        
for a in output:     
    keep=[]
    for b in word_tokenize(str(a['All_text'])):
        b=' '+b
        keep.append(b.replace('\\n', '').replace('\\r','').replace('\\','').replace("\\u",'').replace("xa0",'').replace("'|'",''))
    output1.append(''.join(keep))        
output2=[]
d=0
for c in output:
    output2.append({'url':c['url'],'All_text' :output1[d]})
    d=d+1

output3=[]
stop_words=set(stopwords.words("english"))
for a in output2:
    temp=[]
    for b in word_tokenize(str(a['All_text'])):
        if b not in stop_words:
            b=b+' '
            temp.append(b)
    output3.append(''.join(temp))        

ps=PorterStemmer()
output4=[]
for a in output3:
    temp=[]
    for b in word_tokenize(a):
        t=ps.stem(b)
        t=' '+t
        temp.append(t)
    output4.append(''.join(temp))  

lemmatizer=WordNetLemmatizer()
output5=[]
for a in output4:
    temp=[]
    for b in word_tokenize(a):
        t=lemmatizer.lemmatize(b)
        t=' '+t
        temp.append(t)
    output5.append(''.join(temp))

chk=[] 
r=0
for a in output5:
    d=0
    for b in output5:
        if d>r and d not in chk:
            t=fuzz.token_sort_ratio(a,b)
            if t>90:
                chk.append(d)
        d+=1        
    r+=1;    

output6=[]
b=0
for a in output2:
    if b not in chk:
        output6.append({'url':a['url'],'All_text' :a['All_text']})
    b+=1   

my_file = Path("news.json")
if my_file.exists():
    os.remove('news.json')
with open('news.json', 'a') as outfile:
    json.dump(output6, outfile)