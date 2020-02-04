def even_fibonacci_numbers(n=4000000):
	first = 1
	second = 2
	summation = 0
	while first < n:
		if first % 2 == 0:
			summation += first
		first, second = second, first+second
	return summation

def main():
	result = even_fibonacci_numbers()
	print(result)


if __name__ == '__main__':
	main()
