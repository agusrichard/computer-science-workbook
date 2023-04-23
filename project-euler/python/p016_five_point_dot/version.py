import turtle
import random
import math


def five_point_dot(arm=250, iterations=1000):
	turtle.speed('slowest')
	turtle.penup()
	points = []
	alpha = 18
	for i in range(5):
		point = (arm*math.cos(math.radians(alpha)), arm*math.sin(math.radians(alpha)))
		points.append(point)
		turtle.setpos(point)
		turtle.dot(20, 'blue')
		alpha += 360/5
	position = points[0]
	for i in range(iterations):
		randnum = int(random.uniform(0, 5))
		for j in range(5):
			if randnum == j:
				dx, dy = (points[j][0] - position[0])/2, (points[j][1] - position[1])/2
				break
		position = (position[0] + dx, position[1] + dy)
		turtle.setpos(position)
		turtle.dot(5, 'black')
	turtle.done()

def main():
	five_point_dot(iterations=5)

if __name__ == '__main__':
	main()