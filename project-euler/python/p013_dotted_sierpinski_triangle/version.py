import turtle
import random


def dotted_sierpinski_triangle(iterations=2500):
	turtle.speed('fastest')
	turtle.penup()
	first_dot = (0, 300)
	second_dot = (240, -180)
	third_dot = (-240, -180)
	turtle.setpos(first_dot)
	turtle.dot(20, 'blue')
	turtle.setpos(second_dot)
	turtle.dot(20, 'blue')
	turtle.setpos(third_dot)
	turtle.dot(20, 'blue')
	position = first_dot
	for i in range(iterations):
		die_val = int(random.uniform(0, 6))
		if die_val == 0 or die_val == 1:
			dx, dy = (first_dot[0] - position[0])/2, (first_dot[1] - position[1])/2
		elif die_val == 2 or die_val == 3:
			dx, dy = (second_dot[0] - position[0])/2, (second_dot[1] - position[1])/2
		else:
			dx, dy = (third_dot[0] - position[0])/2, (third_dot[1] - position[1])/2
		position = (position[0] + dx, position[1] + dy)
		turtle.setpos(position)
		turtle.dot(5, 'black')
	turtle.done()
	


def main():
	dotted_sierpinski_triangle()


if __name__ == '__main__':
	main()