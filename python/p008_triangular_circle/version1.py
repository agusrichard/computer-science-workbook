import turtle
import math

turtle.speed('fastest')

def triangular_circle(radius=100, alpha=30):
	reps = int(360/alpha)
	for i in range(reps):
		turtle.forward(radius)
		turtle.left(90)
		turtle.forward(radius*math.tan(math.radians(alpha)))
		turtle.left(90+alpha)
		turtle.forward(radius/(math.cos(math.radians(alpha))))
		turtle.left(180)
	turtle.done()

def main():
	triangular_circle(alpha=5)

if __name__ == '__main__':
	main()