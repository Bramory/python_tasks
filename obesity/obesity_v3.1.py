#!/usr/bin/python
# -*- coding: utf-8 -*-

# graph of dropping the weight

import sys
import math
import matplotlib.pyplot as plt

# import only system from os
from os import system, name

# # define our clear function
# def clear():
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#     else:
#
#     # for mac and linux(here, os.name is 'posix')
#         _ = system('clear')

def num_input(left, right):
    f_val = 0
    while True:
        while True:
            try:
                f_val = float(input())
                break
            except:
                print (' Incorrect input!')
        if f_val < left or f_val > right:
            print (round(left, 0), '< Your Value <', round(right, 0))
        else:
            break
    return f_val

def profile_loading():
    global name
    global start_weight
    global height
    global age
    global activity
    global minutes
    global male
    global cur_weight

    # personal information
    # GREG
    if -1 < name.lower().find('gr'):
        name = 'Greg'
        start_weight = 68
        height = 162
        age = 20
        activity = 3
        minutes = 60
        male = 1
    elif -1 < name.lower().find('pl'):

    # PLATO
        name = 'Plato'
        start_weight = 116
        height = 185
        age = 22
        activity = 4
        minutes = 45
        male = 1
    elif -1 < name.lower().find('br'):

    # BRAMORY
        name = 'Bramory'
        start_weight = 64
        height = 175
        age = 22
        activity = 3
        minutes = 65
        male = 1
    else:
        print (' What is your weight, kg:')
        start_weight = num_input(30, 250)
        print (' What is your height in cm:')
        height = num_input(60, 300)
        print (' What is your age in years:')
        age = num_input(10, 130)
        print (' How much workout days on a week (3, 4, 5...) :')
        activity = num_input(0, 14)
        print (' Your training session in minutes:')
        minutes = num_input(0, 300)
        print (' Are you male (y/n?) :')
        answer = input()
        if answer.find('y') or answer.find('1') or answer.find('+'):
            male = 1
        else:
            male = 0

    cur_weight = start_weight

def info():
    global name
    global cur_weight
    global height
    global age
    global main_consumption
    global avg_losses
    global activity
    global minutes
    global calories_1_train
    global calories_gain
    global def_coeff
    global deficit
    global top_deficit
    global top_proficit
    global ideal_weight

    print ('\n', name, ', continue to upgrade yourself:')
    print ('\n___CHARACTERISTICS___')
    print (' Weight:', round(cur_weight, 0), 'kg')
    print (' Height:', round(height, 0), 'cm')
    print (' Age   :', round(age, 0), 'years')
    print (' Your body consumption    :', round(main_consumption, 0), 'ccal/day')
    print (' Average WITHOUT trainings:', round(main_consumption * 1.3, 0), 'ccal/day')
    print (' Average  WITH   trainings:', round(avg_losses, 0), 'ccal/day')

    print ('\n__Physical trainings__')
    print (' Frequency   :', activity, 'times/week')
    print (' Duration    :', minutes, 'min/workout')
    print (' Energy lose :', round(calories_1_train / minutes * 60, 0), 'ccal/HOUR')

    print ('\n__Recommendations__:')

    #         gaining weight
    if ideal_weight >= cur_weight:
        proficit = calories_gain - avg_losses
        top_proficit = avg_losses * def_coeff
        print (' You gain        :', round(proficit/ccal_in_1g, 0), 'gramm/day')
        print (' proficit can be :', round(top_proficit, 0), 'ccal/day')
        print ('\n Ccal for gaining           :', round(avg_losses, 0) , '-',
                                                round(avg_losses + top_proficit, 0), 'ccal/day')
    else:
    #         losing weight
        print (' You lose        :', round(deficit/ccal_in_1g, 0), 'gramm/day')
        print (' deficit can be:', round(top_deficit, 0), 'ccal/day')
        print ('\n Minimal recommend ccal gain:', round(avg_losses - top_deficit, 0), 'ccal/day')

    print (' Current calories gaining   :', round(calories_gain, 0), 'ccal/day')

def get_main_consumption(
    cur_weight,
    height,
    age,
    male,
    ):
    if male:
        main_consumption = 10 * cur_weight + 6.25 * height - 5 * age + 5
    else:
        main_consumption = 10 * cur_weight + 6.25 * height - 5 * age - 161
    return main_consumption

def do_calculus():
    global cur_weight
    global ideal_weight
    global height
    global age
    global avg_losses
    global main_consumption
    global physical_activity
    global calories_1_train
    global activity
    global deficit
    global calories_gain
    global calories_gain1
    global def_coeff
    global top_deficit
    global minutes
    global LOCK
    global PROCESS

    # Calculate main losses
    main_consumption = get_main_consumption(cur_weight, height, age,
            male)

    # losses for a physical activity
    calories_1_train = 0.014 * cur_weight * minutes * (0.12 * avg_pulse - 7)
    avg_losses = main_consumption * physical_activity + calories_1_train * activity / 7

    # (Losses > gaining) ---> deficit > 0  ---> you drop the weight
    deficit = avg_losses - calories_gain
    top_deficit = avg_losses * def_coeff

    # that's safe to have deficit between 500 and 700 ccal
    if 0 == LOCK:
        #         gaining weight
        if ideal_weight > cur_weight:
            proficit = calories_gain - avg_losses
            top_proficit = avg_losses * def_coeff
            if proficit < 0.1 * avg_losses:
                if ATTENTION:
                    system('cls')
                    print (' Attention!======================================')
                    print (' After ', days, 'days your PROficit =', round(proficit, 0), 'ccal/day')
                    info()
                    print (' Set an appropriate amount of calories:')
                    calories_gain = num_input(0.9 * avg_losses, avg_losses + top_proficit * 1.1)
            else:
                calories_gain = avg_losses + top_proficit
        else:
        #         losing weight
            if deficit < (1 - def_coeff) * top_deficit:
                if ATTENTION:
                    system('cls')
                    print (' Attention!======================================')
                    print (' After ', days, 'days your deficit =', round(deficit, 0), 'ccal/day')
                    info()
                    print (' Reduce your calories:')
                    calories_gain = num_input(avg_losses - top_deficit * 1.1, 1.1 * avg_losses)
                else:
                    calories_gain = avg_losses - top_deficit
    else:
        if (PROCESS) :
            deficit = - avg_losses * (1 +  def_coeff) # for gaining weight
        else :
            deficit = avg_losses - calories_gain1 #only for losing weight

    doIFit(cur_weight)

def doIFit(cur_weight):
    global PROCESS
    global ideal_weight

    if ideal_weight > cur_weight:
        PROCESS = 1 # gaining weight
    else:
        PROCESS = -1 # losing weight

################################################################################
system('cls')
name = input('Hey, what is your name ')  # 'Plato'
ATTENTION = 1  # for playong with calories
def_coeff = 0.3
physical_activity = 1.3  # just eating, sleeping and no working
avg_pulse = 140  # golden rule is 120 - 160 bpm
LOCK = 0

# general GLOBAL values
if True:

    # global values
    start_weight = 100
    cur_weight = start_weight
    height = 180
    age = 33
    activity = 7
    minutes = 25
    male = 1

    calories_deficit = []
    body_consumption = []

    # basic info for the graph
    all_days = []
    all_weights = []
    all_days1 = []
    all_weights1 = []
    all_days2 = []
    all_weights2 = []
    all_days3 = []
    all_weights3 = []
    all_days4 = []
    all_weights4 = []
    all_days5 = []
    all_weights5 = []

    # Caloric Equivalents of Gained or Lost Weight, MAX WISHNOFSKY
    # based on https://academic.oup.com/ajcn/article-abstract/6/5/542/4729975?redirectedFrom=fulltext
    ccal_in_1g = 7.716
    days = 0

profile_loading()

# CALCULATIONS

ideal_weight = (height / 100) ** 2 * 22  # BMI =weight / height (kg/m^2) =21.5

PROCESS = 0
doIFit(cur_weight)
# save flag for catching ideal == current weight
old_process = PROCESS
default_gain = 0
if PROCESS:
    default_gain = 1000  # too less for bodybuilding
else:
    default_gain = 3000 # too much for dropping

calories_gain = default_gain

do_calculus()
day_limit = 365 * 2

if ideal_weight > cur_weight:
    print (' Hey,', name, ', you need to GAIN weight, you looks skinny!')
else:
    print (' Hey,', name, ', you need to LOSE weight, you looks FAT!')

# save info for building a FALSE graph, this is a human's freaquent mistake
if PROCESS:
    deficit1 = top_proficit
    calories_gain1 = avg_losses + top_proficit
else:
    deficit1 = top_deficit
    calories_gain1 = avg_losses - top_deficit

print ('\n Okey, try to go for your ideal weight ', round(ideal_weight, 0), 'kg')
if ATTENTION:
    input('Press any key to continue...')

# simulation1: JUST A THEORY
days = 0
cur_weightN = start_weight
while days < day_limit:
    all_days1.append(days)
    all_weights1.append(cur_weightN)

    if PROCESS != old_process:
        break
    if PROCESS:
        cur_weightN = cur_weightN + deficit1 / ccal_in_1g / 1000  # in kg!
    else:
        cur_weightN = cur_weightN - deficit1 / ccal_in_1g / 1000  # in kg!

    days = days + 1
    doIFit(cur_weightN)
# day_limit =days


# REAL WORLD SIMULATION
days = 0
cur_weight = start_weight
PROCESS = old_process
while days < day_limit:
    all_days.append(days)
    all_weights.append(cur_weight)
    do_calculus()
    calories_deficit.append(deficit)
    body_consumption.append(main_consumption)

    # dropping the weight every night
    if PROCESS != old_process:
        break
    cur_weight = cur_weight - deficit / ccal_in_1g / 1000  # in kg!
    days = days + 1

# PRINT RESULTS
if True:
    system('cls')
    print ('  +++++  RESULTS  +++++')
    print ('\n Days:', days, '== Months:', round(days / 30, 1))
    print (' Weight:', round(cur_weight, 0), 'kg')

    gramms = -1
    try:
        gramms = abs(start_weight - cur_weight) / days * 1000
    except:
        print (' Num of days ====== 0 ')

    if PROCESS:
        print (' You were gain', round(gramms, 0), 'gramms each day')
        print (' Average calories proficit =', round(abs(sum(calories_deficit) / len(calories_deficit)), 0), 'ccal/day')
    else:
        print (' You were drop', round(gramms, 0), 'gramms each day')
        print (' Average calories deficit =', round(abs(sum(calories_deficit) / len(calories_deficit)), 0), 'ccal/day')


    print (' Body consumption =', round(main_consumption, 0), 'ccal')

    print ('\n Physical activity =', round(activity / 7 * days * minutes / 60, 0), 'hours of NOT BEING A BITCH! (do sport)')
    print (' Frequency   :', activity, 'times/week')
    print (' Duration    :', minutes, 'min/workout')

    print ('\n For keeping this weight you should continue to do sport')
    print (' with    sport and eat NOT more than:', round(avg_losses, 0), 'ccal/day')
    print (' without sport and eat NOT more than:', round(avg_losses - activity / 7 * calories_1_train, 0), 'ccal/day')

    print ('\n                              Do not lose all that you\'ve done')

    print (
        'NON REALISTIC STRATEGY:',
        round(cur_weightN - start_weight, 2),
        ' kg in ',
        max(all_days1),
        'days',
        'how people think about dropping the weight',
        )
    print (
        'REAL STRATEGY:                                   ',
        round(cur_weight - start_weight, 2),
        ' kg in ',
        max(all_days),
        'days',
        'that\'s a smart move!',
        )

# simulation2: Real world, but 'calories_gain1' = CONSTANT
days = 0
cur_weight = start_weight
calories_gain = default_gain
LOCK = 1
PROCESS = old_process
while days < day_limit:
    all_days2.append(days)
    all_weights2.append(cur_weight)
    do_calculus()
    if PROCESS != old_process:
        break
    cur_weight = cur_weight - deficit / ccal_in_1g / 1000  # in kg!
    days = days + 1
print (
    'NOT REDUCE CALORIES_LIMIT with PROGRESS:         ',
    round(cur_weight - start_weight, 2),
    ' kg in ',
    max(all_days2),
    'days',
    'common mistake',
    )

# simulation3: WITHOUT changing 'calories_gaining' and
# DROP THE SPORT
days = 0
cur_weight = start_weight
calories_gain = default_gain
activity = 0
LOCK = 1
PROCESS = old_process
while days < day_limit:
    all_days3.append(days)
    all_weights3.append(cur_weight)
    do_calculus()
    if PROCESS != old_process:
        break
    cur_weight = cur_weight - deficit / ccal_in_1g / 1000  # in kg!
    days = days + 1
print (
    'NOT REDUCE and DROP THE SPORT:                   ',
    round(cur_weight - start_weight, 2),
    ' kg in ',
    max(all_days3),
    'days',
    'Does it cost it?',
    )

# simulation4: WITHOUT changing 'calories_gaining'
# EAT piece of cake ==250 ccal
days = 0
cur_weight = start_weight
calories_gain = default_gain
activity = 3
EXTRA_CAKE = 220  # (ccal)
PROCESS = old_process
while days < day_limit:
    all_days4.append(days)
    all_weights4.append(cur_weight)
    do_calculus()
    deficit -= EXTRA_CAKE
    if PROCESS != old_process:
        break
    cur_weight = cur_weight - deficit / ccal_in_1g / 1000  # in kg!
    days = days + 1

print (
    'NOT REDUCE and EAT EXTRA ',
    EXTRA_CAKE,
    ' ccal:             ',
    round(cur_weight - start_weight, 2),
    ' kg in ',
    max(all_days4),
    'days',
    'more easy to shrink calories',
    )

# simulation WITHOUT changing 'calories_gaining'
# and EAT piece of cake ==250 ccal
# and DROP THE SPORT
days = 0
cur_weight = start_weight
calories_gain = default_gain
activity = 0
EXTRA_CAKE = EXTRA_CAKE  # (ccal)
PROCESS = old_process
while days < day_limit:
    all_days5.append(days)
    all_weights5.append(cur_weight)
    do_calculus()
    deficit -= EXTRA_CAKE
    if PROCESS != old_process:
        break
    cur_weight = cur_weight - deficit / ccal_in_1g / 1000  # in kg!
    days = days + 1
print (
    'NOT REDUCE + DROP THE SPORT + EAT EXTRA 220 ccal:',
    round(cur_weight - start_weight, 2),
    ' kg in ',
    max(all_days5),
    'days',
    ' Ah, shit, here we go again!',
    )

input('\n\n___Press any key to show the GRAPH___')
plt.plot(all_days, all_weights)  # REAL WORLD

# plt.plot(all_days, body_consumption)     # REAL WORLD
# plt.plot(all_days, calories_deficit)     # REAL WORLD

plt.plot(all_days1, all_weights1)  # JUST A SIMPLE THEORY
# plt.plot(all_days2, all_weights2)  # REAL but don't reduce calories

plt.plot(all_days3, all_weights3)     # DROP THE SPORT
# plt.plot(all_days4, all_weights4)     # EAT PIECE of CAKE
# plt.plot(all_days5, all_weights5)     # DO BOTH

plt.show()
input('\n Press any key to exit...')

# return all_weights

# from matplotlib.widgets import Slider  # import the Slider widget
#
# import numpy as np
# import matplotlib.pyplot as plt
# from math import pi
#
# a_min =1000    # the minimial value of the paramater a
# a_max =3000   # the maximal value of the paramater a
# a_init =1900   # the value of the parameter a to be used initially, when the graph is created
#
# x =np.linspace(0, 500, 100)
#
# fig =plt.figure(figsize=(5,3))
#
## first we create the general layount of the figure
## with two axes objects: one for the plot of the function
## and the other for the slider
# sin_ax =plt.axes([0.1, 0.2, 0.8, 0.65])
# slider_ax =plt.axes([0.1, 0.05, 0.8, 0.05])
#
#
## in plot_ax we plot the function with the initial value of the parameter a
# plt.axes(sin_ax) # select sin_ax
# plt.title('y =sin(ax)')
# plt.xlim(0, 365)
# plt.ylim(50, 70)
#
## here we create the slider
# a_slider =Slider(slider_ax,      # the axes object containing the slider
#                   'a',            # the name of the slider parameter
#                   a_min,          # minimal value of the parameter
#                   a_max,          # maximal value of the parameter
#                   valinit=a_init  # initial value of the parameter
#                  )
#
## Next we define a function that will be executed each time the value
## indicated by the slider changes. The variable of this function will
## be assigned the value of the slider.
# def update(a):
#     print (' AAAAAAAAAAAAa =', a)
#     update_graph(name, a)
#     sin_ax.set_ydata() # set new y-coordinates of the plotted points
#     fig.canvas.draw_idle()          # redraw the plot
#
## the final step is to specify that the slider needs to
## execute the above function when its value changes
# a_slider.on_changed(update)
#
# plt.show()
