import math
import random
import turtle


def random_walk_vers3(steps=1000):
	turtle.speed('fastest')
	turtle.home()
	for i in range(steps):
		turtle.left(random.uniform(0, 360))
		turtle.forward(random.uniform(0, 10))
	last_post = turtle.position()
	print("The last position: ", last_post)
	distance = math.sqrt(last_post[0]**2 + last_post[1]**2)
	return distance

def main():
	result = random_walk_vers3(100)
	print("The distance is", result)

if __name__ == '__main__':
	main()