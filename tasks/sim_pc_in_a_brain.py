#!/usr/bin/python
# just joggling with numbers
# find nod of the number k 

import sys
import math

def isThisNumberSumOfSquared():
	k = 19451945
	i = j = 0
	n = m = int(math.sqrt(k)) + 1
	print("K = ", n)
	for j in range(j, n): 
		for i in range(i, n):
			if (i*i + j*j == k):
				print("Answer is founded!")
				print(i*i, "+", j*j, "=", k)
				return [i, j]
	print("Answer is not founded!")

print("My return are:", isThisNumberSumOfSquared())


