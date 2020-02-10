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