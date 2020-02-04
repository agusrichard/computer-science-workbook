import math
import sys

def sieve_of_erastothenes(n):
	default_list = list(range(2, n+1))
	for i in default_list:
		j = 2*i
		while j < n+1:
			try:
				default_list.remove(j)
			except ValueError:
				pass
			j += i
	return default_list, len(default_list)

def main():
	result, length = sieve_of_erastothenes(10000)
	print(result)
	print(length)


if __name__ == '__main__':
	main()