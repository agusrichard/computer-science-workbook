import turtle
import random
import math


def five_point_dot(arm=250, num_points=3, iterations=1000):
	turtle.speed('fastest')
	turtle.penup()
	points = []
	alpha = 0
	for i in range(num_points):
		point = (arm*math.cos(math.radians(alpha)), arm*math.sin(math.radians(alpha)))
		points.append(point)
		turtle.setpos(point)
		turtle.dot(20, 'blue')
		alpha += 360/num_points
	position = points[0]
	for i in range(iterations):
		randnum = int(random.uniform(0, num_points))
		for j in range(num_points):
			if randnum == j:
				dx, dy = (points[j][0] - position[0])/2, (points[j][1] - position[1])/2
				break
		position = (position[0] + dx, position[1] + dy)
		turtle.setpos(position)
		turtle.dot(5, 'black')
	turtle.done()

def main():
	five_point_dot(num_points=7)

if __name__ == '__main__':
	main()