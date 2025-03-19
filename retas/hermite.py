import matplotlib.pyplot as plt
import numpy as np

p0x = 0
p0y = 0
p3x = 4
p3y = 4

m0x = 2
m0y = 8
m1x = 6
m1y = -2

points_x = []
points_y = []
t = 0.0

while t <= 1:
    h00 = 2*t**3 - 3*t**2 + 1
    h10 = t**3 - 2*t**2 + t
    h01 = -2*t**3 + 3*t**2
    h11 = t**3 - t**2
    
    x = h00*p0x + h10*m0x + h01*p3x + h11*m1x
    y = h00*p0y + h10*m0y + h01*p3y + h11*m1y
    
    print("(", round(x, 4), ",", round(y, 4), ")")
    points_x.append(x)
    points_y.append(y)
    t += 0.02

plt.figure(figsize=(8, 6))
plt.plot(points_x, points_y, 'b-')
plt.title('Curva de Hermite')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.show()
