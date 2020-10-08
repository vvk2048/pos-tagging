#----------------week2----------------
import os
import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt

dictionary = {}

outputfile = open("shiva.txt","w")

inputfile = open("harsha.txt")

for line in inputfile:
	for word in line.split():	#word is word_tag 
		if word in dictionary:
			dictionary[word] +=1
		else:
			dictionary[word] =1
inputfile.close()

length = len(dictionary)
print ("No. of words in Dictionary= "+str(length)+"\n")

for dict_word, freq in dictionary.items():
	outputfile.write(str(dict_word) + ": " + str(freq) + "\n")

outputfile.close()

#----------------week3----------------

word_dict= {}
tag_dict= {}

for word, freq in dictionary.items():	#word is word_tag
	if word.find("_") != -1:
		arr=word.split("_")
		
		if arr[0] in word_dict:
			word_dict[arr[0]]+=freq
		else:
			word_dict[arr[0]]=freq

		if arr[1] in tag_dict:
			tag_dict[arr[1]]+=freq
		else:
			tag_dict[arr[1]]=freq

#print(word_dict)
#print(tag_dict)

sortedword_dict = sorted(word_dict.items(), key = lambda kv: kv[1])
sortedtag_dict =sorted(tag_dict.items(), key = lambda kv: kv[1])

sortedword_dict.reverse()
sortedtag_dict.reverse()

wordfreqfile = open("vishnu_word.txt", "w")

for i in range(0,10):
	wordfreqfile.write(str(sortedword_dict[i])+"\n")

wordfreqfile.close()

tagfreqfile = open("vishnu_tag.txt", "w")

for i in range(0,10):
	tagfreqfile.write(str(sortedtag_dict[i])+"\n")

tagfreqfile.close()

xt = []
yt = []

for i in range(0,10):
	xt.append(sortedtag_dict[i][0])
	yt.append(sortedtag_dict[i][1])

plt.bar(xt,yt)
plt.show()

x = []
y = []

for i in range(0,10):
	x.append(sortedword_dict[i][0])
	y.append(sortedword_dict[i][1])

plt.bar(x,y)
plt.show()

#----------------week4----------------

prob_word= dict()

word_taglen=len(word_dict)
arrtag = tag_dict.keys()

for word, freq in word_dict.items():	#word_dict : word freq dictionary
	prob_tagdict=dict()
	for tag in arrtag:
		word_tag= word + "_" + tag
		if word_tag in dictionary:
			prob_tagdict[tag] = dictionary[word_tag]/freq	#dictionary : word_tag frequency
		else:
			prob_tagdict[tag]=0.0
	prob_word[word]= prob_tagdict

#print(prob_word)

probabilityfile = open("group.txt","w")

for word,prob in prob_word.items():
	probabilityfile.write(str(word)+": "+str(prob)+"\n"+"\n")

probabilityfile.close()

#----------------week5----------------

d = os.getcwd()
print(d)
l=[]
np=0
c=0
inc=0
os.chdir(d+"/Test-corpus-1")
for (root,dirs,files) in os.walk('.', topdown = True):
	for file in files:
		di = file[:2]
		f = open(d+"/Test-corpus-1/"+"/"+di+"/"+file)
		tree = ET.parse(f)
		root = tree.getroot()
		for item in root.findall('.//w'):
			k=item.attrib['hw']
			t=item.attrib['c5']
			try:
				Dict=prob_word[k]
				key = max(Dict, key=Dict.get)	#????????????????
				l.append(k+"_"+t+" "+k+"_"+key)
				if t==key:
					c=c+1
				else:
					inc=inc+1
			except KeyError:
				l.append("no prediction possible")
				np=np+1

y1=c*100
y1=y1/len(l)
print(y1)
os.chdir(d)
fil=open("final.txt","w")
for i in l:
	fil.write(i.encode('utf8')+"\n")


		