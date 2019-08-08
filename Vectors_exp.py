import math

class Point:
	def __init__(self, pos = False):
		if pos:
			self.x = int(pos[0])
			self.y = int(pos[1])
		else:
			self.x = 0
			self.y = 0
		
		self.points = (self.x, self.y)

	def __add__(self, other):
		return Point((self.x + other.x, self.y + other.y))

	def __iadd__(self, other):
		self.x = self.x + other.x
		self.y = self.y + other.y
		return Point((self.x, self.y))

	def get_angle(self, target):
		num = (target.y - self.y)
		denom = (target.x - self.x) or 0.001
		diff =  math.degrees(math.atan(num / denom))

		if target.x > self.x:
			if target.y > self.y:
				diff = 360 + diff
			else:
				diff = diff

		else:
			if target.y > self.y:
				diff = 180 + diff
			else:
				diff = 180 + diff

		return(diff)

class Vect:
	def __init__(self, x_mag = 0, y_mag = 0):
		self.x_mag = x_mag
		self.y_mag = y_mag

def dist(point1, point2):
	return(math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2))

