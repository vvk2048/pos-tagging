#----------------week2----------------
from matplotlib import pyplot as plt

dictionary = {}

outputfile = open("2.txt","w")

inputfile = open("1.txt")
for line in inputfile:
	for word in line.split():
		if word in dictionary:
			dictionary[word] +=1
		else:
			dictionary[word] =1
inputfile.close()

length = len(dictionary)
outputfile.write("No. of words in Dictionary= "+str(length)+"\n")

for dict_word, freq in dictionary.items():
	outputfile.write(str(dict_word) + ": " + str(freq) + "\n")

outputfile.close()

#----------------week3----------------

word_dict= {}
tag_dict= {}

for word, freq in dictionary.items():
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

wordfreqfile = open("top10wordfreq.txt", "w")

for i in range(0,10):
	wordfreqfile.write(str(sortedword_dict[i])+"\n")

wordfreqfile.close()

tagfreqfile = open("top10tagfreq.txt", "w")

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

# #----------------week4----------------

prob_word= dict()

word_taglen=len(word_dict)
arrtag = tag_dict.keys()

for word, freq in word_dict.items():
	prob_tagdict=dict()
	for tag in arrtag:
		word_tag= word + "_" + tag
		if word_tag in dictionary:
			prob_tagdict[tag] = dictionary[word_tag]/freq
		else:
			prob_tagdict[tag]=0.0
	prob_word[word]= prob_tagdict

#print(prob_word)

probabilityfile = open("4.txt","w")

for word,prob in prob_word.items():
	probabilityfile.write(str(word)+": "+str(prob)+"\n")

probabilityfile.close()