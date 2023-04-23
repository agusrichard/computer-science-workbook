import math
import random

def random_walk_vers2(steps=1000):
	coord = [0, 0]
	for i in range(steps):
		for j in range(2):
			walk = random.uniform(-1, 1)
			coord[j] += walk
		print("The coordinates as step {}: {}".format(i, coord))
	distance = math.sqrt(coord[0]**2 + coord[1]**2)
	return distance

def main():
	result = random_walk_vers2(100)
	print("The distance to initial position is", result)

if __name__ == '__main__':
	main()