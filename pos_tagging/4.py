import os
import xml.etree.ElementTree as ET
from collections import defaultdict
def convert_percentage(share):
    sum1=0
    for i in share:
        sum1+=i
    ans=[];
    for i in share:
        ans.append(i/sum1)
    return ans

def pri_piechart(label,share):
    share=convert_percentage(share)
    figureObject, axesObject = plotter.subplots()
    axesObject.pie(share,labels=label,autopct='%1.2f',startangle=90)
    axesObject.axis('equal')
    plotter.show()
    
def get_probability(share,tag):

    label=[]
    for t in tag:
        label.append(t)
    fre=[]
    k=0
    for t in range(len(label)):
        fre.append(0)
    
    for s in share:
        put=[]
        ma=0
        ans=""
        for t in share[s]:
            if ma<share[s][t] :
                ma=share[s][t]
                ans=t
            put.append(share[s][t])
        put=convert_percentage(put)
        i=0;
        for t in share[s]:
            share[s][t]=put[i]
            i=i+1
        
        for i in range(len(label)):
            if label[i]==ans:
                fre[i]=fre[i]+1
    print(fre) 
    
    pri_piechart(label,fre)         

    return share 

def prob(word,tag,freq):
    tot=0
    for i in freq[word]:
        tot+=freq[word][i]
    return freq[word][tag]/tot

    
folder = "/home/harsha/Downloads/Assignment-files/Train-corups/"
out = open("/home/harsha/Downloads/Preprocessed_file.txt", "w",encoding='utf-8')
file = os.walk(folder)
dictionary={}
tag={}
probability=defaultdict(lambda : defaultdict(int))

for files in os.walk(folder):

    for file in files:
        tree = ET.parse(folder+file)
        root = tree.getroot()
        for w in root.iter('w'):
            s=w.text.strip().lower()
            ta= w.attrib['pos']
            
            if ta in tag:
                tag[ta]=tag[ta]+1
            else:
                tag[ta]= 1
                
            if s in dictionary:
                dictionary[s]=dictionary[s]+1
            else:
                dictionary[s]= 1
                
                
    for s in  dictionary:
        for t in tag:
            probability[s][t]=0
            
    for file in files:
        tree = ET.parse(folder+file)
        root = tree.getroot()
        for w in root.iter('w'):
            s=w.text.strip().lower()
            ta= w.attrib['pos']
            probability[s][ta]=probability[s][ta]+1
     
    tool=probability
    probability=get_probability(probability,tag)