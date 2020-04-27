#!/usr/bin/python
# strategy of guessing number in a range

import sys
import math
import matplotlib.pyplot as plt
import random
random.seed()

print("I\'m a GuessingMachine:\n")

min = 0
max = 10


# GuessingMachine
guessedNumber = random.randint(min, max)
# print("\nGuessed number:", guessedNumber)

DEBUG = 0
exp = 10000
total_steps = 0
freq = []
for n in range(0, int(max)):
	freq.append(0)

dict = {}

# method:
coeff = 0.8
guess = round((max+1) * coeff) #round((max + min) / 2) #
if DEBUG:
	print("PRINT: ", guess)
for times in range(0, exp):
	
	## for random methods
	list = []
	for x in range(min, max+1):
		list.append(x)


	guess = round((max+1) * coeff) #round((max + min) / 2) #
	guessedNumber = random.randint(min, max)
	tmp_min = min
	tmp_max = max
	steps = 0
	if DEBUG:
		list = []
		for x in range(min, max+1):
		    list.append(x)
		print(list)
	while True:
		steps += 1

		if guess == guessedNumber:
			if DEBUG:
				print("\nGotcha:", guess)
			freq[steps] += 1
			total_steps += steps
			dict[guess] = steps
			break 

		if guess > guessedNumber:
			if DEBUG:
				print("\nShrink UP:")
				for index in range(guess, tmp_max+1):
					list[index] = {}
				print(list)

			tmp_max = guess
			delta = -(tmp_max - tmp_min) * coeff
		else:
			if DEBUG:
				print("\nShrink DOWN:")
				for index in range(tmp_min, guess+1):
					list[index] = []
				print(list)
			tmp_min = guess
			delta = (tmp_max - tmp_min) * coeff #1-coeff

		if steps == 1000:
			print("\nI think:", guess)
			print("Guessed:", guessedNumber)

			break
	
		if delta <= 1 and delta > 0:
			delta = 1
		
		elif delta >= -1 and delta < 0:
			delta = -1
			
		guess = guess + round(delta)
		
		if DEBUG:
			print("PRINT: ", guess)

		# Random method #1
		# guess = random.randint(min, max)

		# Random method #2
		# guess = random.choice(list)
		# list.remove(guess)

print("Based on :", exp," experiments")
print("for range ", [min, max] )
# print("Total steps:", total_steps)
print("Average steps:", total_steps / exp)


# freaquacies of path's longevity
sum = 0
num = []
for i in range (0, int(max)):
	num.append(i)
	if freq[i]:
		sum += freq[i]

print(num)
for i in range (0, int(max)):
	if freq[i]:
		freq[i] = freq[i] / sum * 100
		print(i, ":", round(freq[i], 2))


# how far is this
ind  = []
num2 = []
for i in range (0, max+1):
	ind.append(i)
	num2.append(dict[i])
# print(dict.keys())
# print(dict.values())

# plt.plot(num, freq)     # freq of the steps
plt.plot(ind, num2)     # frequancies of the numbers

plt.show()


# on 1 mill Answers are:
# 0.5   = 6.062373 - 6.063843 times, max = 7 steps  (round)
# 0.618 = 6.236717 - 6.239472 times, max = 10 steps (round)  6.148947 - 6.151854                       (int)
# 0.8   = 8.098662 - 8.106489 times, max = 17 steps (round)  7.516338 - 7.521932 times, max = 20 steps (int)

# FIXED for 1 million experiments
# 0.5   = 5.798171 - 5.800569 times, max = 7 steps  (round)
# 0.618 = 5.998718 - 6.000963 times, max = 8 steps (round)  5.897489 - 5.903117                       (int)
# 0.8   = 7.460297 - 7.46077  times, max = 15 steps (int)

# random 100k:
# average: 99.58399 - 100.13032

# random 100k with excluding:
# average: 50.91152 - 51.11931

# for 1 mill
# 0.5   0-999: 8.988602
# 0.618 0-999: 9.277956