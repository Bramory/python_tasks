#!/usr/bin/python
# probability sort machine

import sys
import math
import matplotlib.pyplot as plt
import random
random.seed()

print("I\'m a Parker Machine! Wshhhh:\n")

total = 100
percent = 0.03
prize = percent * total
trash = total - prize

# Parker Machine
accuracy = 0.95 # probability

print("Prizes:", round(prize, 2))
print("Trash :", round(trash, 2))
print("Total :", round(total, 2))


print("\nWin  chance:", round(prize / total * 100, 2), "%")
print("Lose chance:",   round(trash / total * 100, 2), "%")

exp = 1

win_in_good  = []
lose_in_good = []
list_accuracy = []

accuracy = 0
for accuracy in range(0, 101, 1):
	accuracy = accuracy / 100
	list_accuracy.append(accuracy)

	prize_in_good = accuracy * prize
	trash_in_good = (1 - accuracy) * trash

	prize_in_bad = (1 - accuracy) * prize
	trash_in_bad = accuracy * trash

	good_pile = prize_in_good + trash_in_good # (1-accuracy) * total
	bad_pile  = trash_in_bad  + prize_in_bad  #    accuracy  * total

	if exp == 0:
		print("\nGood pile:")
		print("Win  chance:",  round(prize_in_good / good_pile * 100, 2), "%")
		print("Lose chance:", round(trash_in_good / good_pile * 100, 2), "%")

		print("\nBad pile:")
		print("Win  chance:",  round(prize_in_bad  /  bad_pile * 100, 2), "%")
		print("Lose chance:", round(trash_in_bad  /  bad_pile * 100, 2), "%")

	win_in_good.append (round(prize_in_good / good_pile * 100, 2))
	lose_in_good.append(round(trash_in_good / good_pile * 100, 2))

plt.plot(list_accuracy, win_in_good)     # x, y
plt.plot(list_accuracy, lose_in_good)     # x, y

plt.show()
