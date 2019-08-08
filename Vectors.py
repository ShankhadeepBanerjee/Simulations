import math

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

