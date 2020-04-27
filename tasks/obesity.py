#!/usr/bin/python
# graph of dropping the weight

import sys
import math
import matplotlib.pyplot as plt

# basic info for the graph
all_days = []
all_weights = []
calories_deficite = []
body_consumption = []

name = input("Hey, what is your name ")

# personal information
# GREG
if 'greg' == name.lower(): 
	start_weight = 69 #input("What is your weight, kg?")
	cur_weight = start_weight  
	height     = 165 #input("What is your height, m?")
	age        = 20  #input("What is your age, years?")
	activity   = 3   #input("What is your activity (3, 4, 5 times in a week)?")
	minutes    = 60  #input("How long is your training session?")
	male       = 1

# PLATO
elif name.lower() == 'plato': 
	start_weight = 100 #input("What is your weight, kg?")
	cur_weight = start_weight  
	height     = 180 #input("What is your height, m?")
	age        = 22  #input("What is your age, years?")
	activity   = 4   #input("What is your activity (3, 4, 5 times in a week)?")
	minutes    = 45  #input("How long is your training session?")
	male       = 1

# BRAMORY
elif name.lower() == 'bramory': 
	start_weight = 64 #input("What is your weight, kg?")
	height     = 175 #input("What is your height, m?")
	age        = 22  #input("What is your age, years?")
	activity   = 3   #input("What is your activity (3, 4, 5 times in a week)?")
	minutes    = 65  #input("How long is your training session?")
	male       = 1

else:
	start_weight = input("What is your weight, kg?")
	cur_weight = start_weight  
	height     = input("What is your height, m?")
	age        = input("What is your age, years?")
	activity   = input("What is your activity (3, 4, 5 times in a week)?")
	minutes    = input("How long is your training session?")
	answer     = input("Are you a male?")
	if answer.find('y') or answer.find('1') or answer.find('+'):
		male = 1
	else:
		male = 0
start_weight = float(start_weight)
cur_weight = float(start_weight)  
height     = float(height) 
age        = float(age) 
activity   = float(activity) 
minutes    = float(minutes) 

calories_gain = 9999
ideal_weight = (height/100) ** 2 * 21.5 # BMI = weight / height (kg/m^2) = 21.5

if ideal_weight > cur_weight:
	print("Hey, ", name ,", you need to GAIN weight!!!")
	print("Your ideal weight is", round(ideal_weight, 2), "kg")
	exit()

days = 0
ccal_in_1g = 7.2
avg_pulse = 140
physical_activity = 1.3 # just eating, sleeping and no working

print("Hi ", name,"! This is your beginning stats:")
print("Current weight:", round(cur_weight, 2), "kg")
print("Current height:", round(height, 2), "cm")
print("Current    age:", round(age, 2), "years")
print("Current calories gaining = ", round(calories_gain, 2), "ccal")
main_consumption = 10 * cur_weight + 6.25 * height - 5 * age + 5
print("Body consumption = ", round(main_consumption, 2), "ccal")
print("real Body consumption = ", round(main_consumption * 1.3, 2), "ccal")
calories_1_train = 0.014 * cur_weight * minutes * (0.12 * avg_pulse - 7) 
avg_losses = main_consumption * physical_activity + calories_1_train * activity / 7
print("losses per day with", activity ," training per week = ", round(avg_losses, 2), "ccal")
deficite = avg_losses - calories_gain 
print("Deficite = ", round(deficite, 2), "ccal")
print("\nWe are starting to go for a ", round(ideal_weight, 2), "kg")

while cur_weight > ideal_weight:	
	all_days.append(days)
	all_weights.append(cur_weight)
	
	#Calculate main losses
	# base need of the body
	if male:
		main_consumption = 10 * cur_weight + 6.25 * height - 5 * age + 5
	else:
		main_consumption = 10 * cur_weight + 6.25 * height - 5 * age - 161

	# losses for a physical activity
	calories_1_train = 0.014 * cur_weight * minutes * (0.12 * avg_pulse - 7) 

	# (Losses > gaining) ---> deficite > 0  ---> you drop the weight
	avg_losses = main_consumption * physical_activity + calories_1_train * activity / 7
	deficite = avg_losses - calories_gain 
	calories_deficite.append(deficite)
	body_consumption.append(main_consumption)


	# that's safe to have deficite between 500 and 700 ccal
	if deficite < 300:
		print("\nAttention!")
		print("Your current weight = ", round(cur_weight, 2), "kg")
		print("after = ", days, "days")
		print("Current calories gaining = ", round(calories_gain, 2), "ccal")
		print("Body consumption = ", round(main_consumption, 2), "ccal")
		print("calories_1_train = ", round(calories_1_train, 2), "ccal")
		print("average losses per day = ", round(avg_losses, 2), "ccal")
		print("Deficite = ", round(deficite, 2), "ccal")
		try: 
			new_val = input("Please, reduce your calories! Calories gaining = ")
		except:
			print("This is not a number!")
		calories_gain = float(new_val)

	cur_weight = cur_weight - (deficite / ccal_in_1g / 1000) # in kg!
	days = days + 1

print("\n\n\n   +++++  RESULTS  +++++")
print("\nDays:", days, " == Months:", round(days / 30, 1))
print("Weight:", round(cur_weight, 2), "kg")
print("You were drop", round((start_weight - cur_weight) / days * 1000, 2), "gramms each day")
print("Average calories deficite = ", round(sum(calories_deficite) / len(calories_deficite), 2), "ccal/day")
print("Body consumption = ", round(main_consumption, 2), "ccal")

print("\nPhysical activity = ", round(activity / 7 * days * minutes / 60, 2), "hours not of being a bitch!")
print("Times in a week:", activity)
print("Minutes per training:", minutes)

print("\nFor keeping this weight you should continue to do sport")
print("and gain calories NOT bigger than:", round(avg_losses, 2), "ccal per day")

print("OR without sport  NOT bigger than:", round(avg_losses - activity/7 * calories_1_train, 2), "ccal per day")



# print("Days: ", all_days)
# print("Days: ", all_weights)

# i = 0
# for kg in all_weights:
# 	kg = kg * 100
# 	all_weights(i) = kg
# 	i = i + 1

plt.plot(all_days, all_weights)     # x, y
# plt.plot(all_days, calories_deficite) # x, y
# plt.plot(all_days, body_consumption) # x, y

plt.show()
