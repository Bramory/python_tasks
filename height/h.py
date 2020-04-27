import math

g = 9.805
m = 1.0 # kg
p_obj = 1000 #density of the object
V = m / p_obj # m^3 4/3 * math.pi * R^3
R = (V*3 / math.pi / 4 ) ** (1/3)
h = 10000 # metres

# I think form will deform from circle to "square"
A = math.pi * R**2 * (4/math.pi) # Area perpendicular to velocity
C = 0.95 # sphere = 0.5, cube = 1.05 
p0 = 1.225 #density of the air
v = math.sqrt( (2 * m * g) / (p0 * A * C) ) # km/h
drag_force = (p0 * C * A * v**2) / 2

print("Velocity =", round(v * 3.6, 2), "km/h")

t_vacuum = math.sqrt(2*h/g)
speed_up_time = math.sqrt(2 * v / g)
t_air = (h / v) + speed_up_time
print("Time for falling in vacuum =", round(t_vacuum, 2), "s")
print("in the air (at least)", round(t_air, 2), "s")
print("h =", round(h, 2), "m")
print("Radius of the ""sphere"" =", round(R*100, 2), "cm")
pot_en = m * g * h
print("Potential energy", round(pot_en, 2), "N")
kinet_en = m * v**2 / 2
print("Kinetic energy", round(t_air, 2), "N")

print("Area =", round(A, 2), "m^2, Pressure =", round(kinet_en / A, 2), "kg / m^2 ??" )
print("Drag force =", round(drag_force, 2), "N")
print("Gravity force =", round(m * g, 2), "N")

a = input("bye")
