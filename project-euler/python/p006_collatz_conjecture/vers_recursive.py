import sys

def collatz_conjecture_recursive(num):
	print("The number is", num)
	if num == 1:
		return
	elif num % 2 == 0:
		collatz_conjecture(num / 2)
	else:
		collatz_conjecture(3*num + 1)
	


def main():
	collatz_conjecture_recursive(int(sys.argv[1]))

if __name__ == '__main__':
	main()