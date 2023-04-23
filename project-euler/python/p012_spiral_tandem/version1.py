import turtle



def spiral_tandem(radius=[1, 2], spiral_difference=[0.1, 0.11], alpha=10, level=10):
	t1 = turtle.Turtle()
	t2 = turtle.Turtle()
	t1.speed('fastest')
	t2.speed('fastest')
	reps = int(360/alpha)
	for i in range(reps*level):
		t1.forward(radius[0])
		t2.forward(radius[1])
		t1.left(alpha)
		t2.left(alpha)
		radius[0] += spiral_difference[0]
		radius[1] += spiral_difference[1]
	turtle.done()
	
		

def main():
	spiral_tandem()

if __name__ == '__main__':
	main()


import turtle
import math

turtle.speed('fastest')

def spiral(radius=1, spiral_difference=0.25, alpha=10, level=10):
	reps = int(360/alpha)
	for i in range(reps*level):
		turtle.forward(radius)
		turtle.left(alpha)
		radius += spiral_difference
	turtle.done()

def main():
	spiral(spiral_difference=0.1)

if __name__ == '__main__':
	main()