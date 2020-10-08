import os
import xml.etree.ElementTree as ET

d = os.getcwd()
l=[]
os.chdir(d+"/Train-corups-1")
for (root,dirs,files) in os.walk('.', topdown = True):
    for file in files:
        di = file[:2]
        f = open(d+"/Train-corups-1/"+"/"+di+"/"+file)
        tree = ET.parse(f)
        root = tree.getroot()
        for item in root.findall('.//w'):    #??????????????????????????
            key=item.attrib['hw']
            l.append(item.attrib['hw']+"_"+item.attrib['c5'])

print(len(l))
os.chdir(d)
print(os.getcwd())
file=open("harsha.txt",'w')
for i in l:
    file.write(i.encode('utf8')+"\n")