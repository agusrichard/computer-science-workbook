import turtle
import random

def two_point_dot(iterations=1000):
	turtle.speed('fastest')
	turtle.penup()
	first_dot = (500, 0)
	second_dot = (-500, 0)
	turtle.setpos(first_dot)
	turtle.dot(20, 'blue')
	turtle.setpos(second_dot)
	turtle.dot(20, 'blue')
	position = first_dot
	for i in range(iterations):
		die_val = int(random.uniform(0, 6))
		if die_val == 0 or die_val == 1 or die_val == 2:
			dx, dy = (first_dot[0] - position[0])/2, (first_dot[1] - position[1])/2
		else:
			dx, dy = (second_dot[0] - position[0])/2, (second_dot[1] - position[1])/2
		position = (position[0] + dx, position[1] + dy)
		turtle.setpos(position)
		turtle.dot(3, 'black')
	turtle.done()

def main():
	two_point_dot()

if __name__ == '__main__':
	main()