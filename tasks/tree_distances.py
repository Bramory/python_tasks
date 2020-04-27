#!/usr/bin/python
# distances between top and bottom of the trees 
# on the different spots of the Earth 

# started from the equator (0 degree) to the polar (90 degree)

import sys
import math
import matplotlib.pyplot as plt

# F - geocentric
# B - geodetic
# correlation between these angles:
# math.tan(B) = a ** 2  / b ** 2 * math.tan(F * math.pi / 180)


# input : geodetic   angle in degrees
# output: geocentric angle in radians
def getGeoDetic(r_pol, r_eq, geocentric_angle):
	a = r_eq
	b = r_pol
	# f = (a - b) / a
	#print('See this: !!!!!', (1-f) * (1-f))
	#print('See this: !!!!!', (b ** 2 / a ** 2))

	geodetic_angle = math.atan( (a / b) ** 2 * math.tan(geocentric_angle * math.pi / 180)) 
	return geodetic_angle

#return radius for spheroid
# pay attention that geodetic and geocentric latitude are different
# maximum diff = 11.5' ~= 0.19 degrees on F = 45 degree
def radius(r_pol, r_eq, geocentric_angle):
	a = r_eq
	b = r_pol
	F0 = getGeoDetic(r_pol, r_eq, geocentric_angle)
	num   = (a ** 2 * math.cos(F0)) ** 2 + (b**2 * math.sin(F0)) ** 2 
	denum = (a      * math.cos(F0)) ** 2 + (b    * math.sin(F0)) ** 2 
	r0 = math.sqrt(num / denum)
	return r0

print ("Hello")
#k = int(sys.argv[1])
#if (arg <= 1):


# FIXED STATIONARY POINT!!!
p1 = r_pol = 6356.78 #polar radius in KM

# DYNAMIC POINT FOR CALC!!!
p2 = r_eq = 6378.137 #equator radius
H1 = 2000 / 1000 # height of a 1-st tree
H2 = 2 / 1000 # height in KiloMetres

angles = []
tops = []
bots = []
tops2 = []
bots2 = []
diff = []
fixed = []

#  depends on H1, B1 (and optionally on L1 * math.pi / 180)
# STATIONARY POINT: 90 degree
_in_rad = math.pi / 180.0			
B1 = getGeoDetic(r_pol, r_eq, 0.0)
L1 = 0 * _in_rad

po1 = (r_eq ** 2) / (math.sqrt(r_eq ** 2 * math.cos(B1) ** 2 + r_pol ** 2 * math.sin(B1) ** 2))
x_bot1 = po1 * math.cos(B1) * math.cos(L1)
y_bot1 = po1 * math.cos(B1) * math.sin(L1)
z_bot1 = po1 * (r_pol/r_eq) ** 2 * math.sin(B1)

x_top1 = (po1 + H1) * math.cos(B1) * math.cos(L1)
y_top1 = (po1 + H1) * math.cos(B1) * math.sin(L1)
z_top1 = (po1 * (r_pol/r_eq) ** 2 + H1) * math.sin(B1)

# start from South pole through equator to the North pole
delta = 0.001
angle = 0.0

while angle < 90:	
	# if (angle > -1) and (angle < 1):
	angles.append(angle)
	p2 = radius(r_pol, r_eq, angle) # in degrees

	# bullshit ?
	angle_coeff = math.cos(angle * _in_rad) # in radians
	
	#simplest method - cosine theorem:
	try:
		c_top = math.sqrt((p1 + H1) ** 2 + (p2 + H2) ** 2 - 2 * (p1 + H1) * (p2 + H2) * angle_coeff)
		c_bot = math.sqrt( p1       ** 2 +  p2       ** 2 - 2 *  p1       *  p2       * angle_coeff)
	except:
		print('SQRT get smth bad!')

	# Let's start 
	# STATIONARY POINT
	B2 = getGeoDetic(r_pol, r_eq, angle)
	L2 = 0 * _in_rad
	po2 = (r_eq ** 2) / (math.sqrt(r_eq ** 2 * math.cos(B2) ** 2 + r_pol ** 2 * math.sin(B2) ** 2))

	x_bot2 = po2 * math.cos(B2) * math.cos(L2)
	y_bot2 = po2 * math.cos(B2) * math.sin(L2)
	z_bot2 = po2 * (r_pol/r_eq) ** 2 * math.sin(B2)

	x_top2 = (po2 + H2) * math.cos(B2) * math.cos(L2)
	y_top2 = (po2 + H2) * math.cos(B2) * math.sin(L2)
	z_top2 = (po2 * (r_pol/r_eq) ** 2 + H2) * math.sin(B2)

	# coord for point that goes straight from the center of the ellipsoid!,
	# that's why we use here "angle"
	x_top3 = x_bot2 + H2 * math.cos(angle * _in_rad) * math.cos(L2)
	y_top3 = y_bot2 + H2 * math.cos(angle * _in_rad) * math.sin(L2)
	z_top3 = z_bot2 + H2 * math.sin(angle * _in_rad)
	fix = 1000 * math.sqrt((x_top2 - x_top3) ** 2 + (y_top2 - y_top3) ** 2 + (z_top2 - z_top3) ** 2)
	fixed.append(fix)

	# calc distance
	c_top2 = math.sqrt((x_top2 - x_top1) ** 2 + (y_top2 - y_top1) ** 2 + (z_top2 - z_top1) ** 2)
	c_bot2 = math.sqrt((x_bot2 - x_bot1) ** 2 + (y_bot2 - y_bot1) ** 2 + (z_bot2 - z_bot1) ** 2)

	k = 45.0
	if (angle <= k + 2 * delta) and (angle >= k - 2 * delta):
		print('\nAngle_coeff = ', angle_coeff)
		print ("[angle ", angle, " diff = ", (c_top2 - c_bot2) * 1000, ' metres' )
		print('Radius = ', p2)
		print('geodetic = ', B2 * 180 / math.pi, 'degrees')
		# print ('po 1|2 :', po1, '  ', po2)
		# print ('X_bot 1|2 :', x_bot1, '  ', x_bot2)
		# print ('X_top 1|2 :', x_top1, '  ', x_top2)
		# print ('Y 1|2 :', y_bot1, '  ', y_bot2)
		# print ('Y 1|2 :', y_top1, '  ', y_top2)
		# print ('Z 1|2 :', z_bot1, '  ', z_bot2)
		# print ('Z 1|2 :', z_top1, '  ', z_top2)
		# print ('\n\nTOP_LINE: old|new :', c_top, 'km  ', c_top2, ' KM')
		# print ('BOT_LINE: old|new :', c_bot, 'km  ', c_bot2, ' KM')
		# calc imagine distance for sphere and spheroid.
		print ("coord ", x_top2 - x_top3, y_top2 - y_top3, z_top2 - z_top3)
		print ("fixing top position for spheroid: ", fix, 'metres')
		# bullshit
		# print ("just a sub of distances         : ", 1000 * (c_top2 - c_top), 'metres')

	bots.append(c_bot)
	tops.append(c_top)

	bots2.append(c_bot2)
	tops2.append(c_top2)


	# if (angle > -1) and (angle < 1):
	diff.append((c_top2 - c_bot2) * 1000) #metres diff between top and bot
	# print("\ntop2:", c_top2, c_top, 'metres')
	angle = round(angle + delta, 4)
	# END OF WHILE LOOP

print("\nMIN :", min(diff), 'metres')
in1 = diff.index(min(diff))
print("Index :", in1)
print("angle :", angles[in1], 'degrees')
print("MAX :", max(diff), 'metres')

print("\n\n\nFIXED")

print("\nMIN :", min(fixed), 'metres')
print("MAX :", max(fixed), 'metres')
in1 = fixed.index(max(fixed))
print("Index :", in1)
print("angle :", angles[in1], 'degrees')


plt.plot(angles, diff) ## x, y
# plt.plot(angles, fixed) ## x, y

# plt.plot(angles, tops) ## x, y
# plt.plot(angles, bots) ## x, y

# plt.plot(angles, tops2) ## x, y
# plt.plot(angles, bots2) ## x, y

plt.show()


