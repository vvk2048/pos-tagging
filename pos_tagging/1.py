import os
import xml.etree.ElementTree as ET


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

d = os.getcwd()
l = []
os.chdir(d + "/Train-corups-2")

files = getListOfFiles(d + "/Train-corups-2")

for f in files:

    fil = open(f)
    tree = ET.parse(fil)
    root = tree.getroot()

    for item in root.findall('.//w'):
        l.append(item.text.strip() + "_" + item.attrib['pos'])

print(len(l))
os.chdir(d)
f = open("1.txt", 'w')
for i in l:
    f.write(i)
    f.write("\n")