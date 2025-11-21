import math;

def circleStats(radius):
	area=math.pi*(radius**2)
	circumference=2*math.pi*radius
	return area, circumference

a, c = circleStats(5)

print('area',round(a, 2))
print('circumference', round(c, 2))