import sys

def collatz_conjecture_iteration(num):
	reps = 0
	while True:
		print("The number is", num)
		if num == 1:
			break
		elif num % 2 == 0:
			num /= 2
			reps += 1
		else:
			num = 3*num + 1
			reps += 1

	return reps


def main():
	result = collatz_conjecture_iteration(int(sys.argv[1]))
	print("The number of steps to base(1) is", result)

if __name__ == '__main__':
	main()
