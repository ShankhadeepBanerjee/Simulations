import math


class Vector2D:
	def __init__(self, startpoint, mag = 1, angle = 0):
		self.x = startpoint.x
		self.y = startpoint.y
		self.mag = mag
		self.angle = angle
		self.endx = (self.x + self.mag * math.cos(math.radians(self.angle)))
		self.endy = (self.y - self.mag * math.sin(math.radians(self.angle)))



	def __repr__(self):
		return("Vector2D(%s, %s)" % (self.x, self.y))

	def angle_between(self, othervect):
		num = (self.x * othervect.x + self.y * othervect.y)
		dinom = (self.mag * othervect.mag)
		return(math.acos(num/dinom))


class Point:
	def __init__(self, pos):
		self.x = int(pos[0])
		self.y = int(pos[1])
		self.points = (self.x, self.y)

	def get_angle(self, target):
		num = -(target.y - self.y)
		denom = (target.x - self.x) or 0.000001
		diff =  math.degrees(math.atan(num / denom))
		return(diff)

def dist(point1, point2):
	return(math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2))

def angle_in_points(point1, point2):
	num = -(point2.y - point1.y)
	denom = (point2.x - point1.x) or 0.000001
	diff =  math.degrees(math.atan(num / denom))
	return(diff)



# a = Vector2D(2,3,5,50)
# print(a.endx, a.endy)