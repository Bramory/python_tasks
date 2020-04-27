#!/usr/bin/python
# how many steps frog need to jump on average if she junp
#  random distance from those dist that left ?

import sys
import math
import matplotlib.pyplot as plt
import random

DIST = 10
random.seed()
print("I\'m a frog")

total_steps = 0
exp = 400
i = 0

distances = []
avg_jumps = []
for DIST in range(1, 1000+1):
	distances.append(DIST)
	total_steps = 0
	for i in range(exp):
		dist_left = DIST
		while dist_left > 0:
			covered = random.randint(1, dist_left) #min, max
			# print("Random number:", jump)
			dist_left = dist_left - covered
			total_steps += 1
	avg_jumps.append(total_steps / exp)

# print("Steps:", total_steps, steps)
print("Based on :", exp," experiments")
print("for distance:", DIST)
print("Average steps:", total_steps / exp)

# plot this function
plt.plot(distances, avg_jumps)     # frequancies of the numbers
plt.show()

# Answer is 2.926907   - 2.93066   # 1 mill   /2.7s
# Answer is 2.9284423  - 2.9290662 # 10 mill
# Answer is 2.92886304 - 2.93066   # 100 mill /270.4s
