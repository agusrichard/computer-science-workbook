import turtle
import math

turtle.speed('fastest')

def triangular_spiral(radius=1, spiral_difference=0.25, alpha=10, level=10):
	reps = int(360/alpha)
	for i in range((2*reps)*level):
		turtle.forward(radius)
		turtle.left(90)
		turtle.forward(radius*math.tan(math.radians(alpha)))
		turtle.left(90+alpha)
		turtle.forward(radius/(math.cos(math.radians(alpha))))
		turtle.left(180-(alpha/2))
		radius += spiral_difference
	turtle.done()

def main():
	triangular_spiral()

if __name__ == '__main__':
	main()