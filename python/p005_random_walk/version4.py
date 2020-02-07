import random
import math
import sys

def random_walk_vers4(dist, reps=1000):
	for i in range(reps):
		x, y = 0, 0
		counter = 0
		while True:
			distance = math.sqrt(x**2 + y**2)
			if distance >= dist:
				break
			else:
				dx, dy = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
				x += dx
				y += dy
				counter += 1
		print("Reps:{}, steps: {}".format(i, counter))


def main():
	random_walk_vers4(int(sys.argv[1]), reps=int(sys.argv[2]))

if __name__ == '__main__':
	main()