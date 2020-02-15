import turtle
import random

def four_point_dot(iterations=1000):
	turtle.speed('fastest')
	turtle.penup()
	first_dot = (100, 100)
	second_dot = (100, -100)
	third_dot = (-100, -100)
	fourth_dot = (-100, 100)
	turtle.setpos(first_dot)
	turtle.dot(20, 'blue')
	turtle.setpos(second_dot)
	turtle.dot(20, 'blue')
	turtle.setpos(third_dot)
	turtle.dot(20, 'blue')
	turtle.setpos(fourth_dot)
	turtle.dot(20, 'blue')
	position = first_dot
	for i in range(iterations):
		die_val = random.randint(0, 3)
		if die_val == 0:
			dx, dy = (first_dot[0] - position[0])/2, (first_dot[1] - position[1])/2
		elif die_val == 1:
			dx, dy = (second_dot[0] - position[0])/2, (second_dot[1] - position[1])/2
		elif die_val == 2:
			dx, dy = (third_dot[0] - position[0])/2, (third_dot[1] - position[1])/2
		else:
			dx, dy = (fourth_dot[0] - position[0])/2, (fourth_dot[1] - position[1])/2
		position = (position[0] + dx, position[1] + dy)
		turtle.setpos(position)
		turtle.dot(5, 'black')
	turtle.done()

def main():
	four_point_dot()

if __name__ == '__main__':
	main()