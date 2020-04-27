fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	t = line.split()
	for word in t:
    	for i in range(len(t)):
			if word not in lst:
				lst.append(word)
lst.sort()
print(lst)
