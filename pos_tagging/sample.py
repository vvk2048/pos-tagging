a = list()
a.append(1)
a.append(4)
filen = open("random.txt", "w")
filen.write(str(a))
filen.close()
filer =open("random.txt", "r")
string = filer.read()
print(string)
l = eval(string)
print(l[0])