#!/usr/bin/python
# probability that N people habe match of their
# birthdays

import sys
import matplotlib.pyplot as plt



def bd(k = 2):
	print ("Hello")
	#k = int(sys.argv[1])
	if (k <= 1):
		print("There is no humans")
		return

	P = 1.0
	if (k > 364):
		return P;	
	for i in range(1, k):
		P *= (365 - i) / 365.0
		print (365 - i, "/", 365.0)
	print("real probability for match:", 1-P);

	#P = 1.0
	#for i in range(0, i):
	#	P *= (365 - i) / (365-i+1)
	#print("Probability that no one match :",   P)
	#printProbability that no one match :",   P)
	#print("("P at least 1 match in the bd  :", 1-P)


	return 1-P;


q = int(sys.argv[1])
N = []
probability = [	]
for i in range(2, q+1):
	print(i, "\n")
	N.append(i)
	probability.append(func(i))
print(N)
print(probability)

plt.plot(N, probability)
plt.show()


