def multiples_of_x_and_y(x, y, n=1000):
	x_list, y_list = [x], [y]
	while x_list[-1] < 1000-x:
		x_list.append(x_list[-1] + x)
	while y_list[-1] < 1000-y:
		y_list.append(y_list[-1] + y)
	true_list = set(x_list) | set(y_list)
	return sum(list(true_list))

def main():
	summation = multiples_of_x_and_y(3, 5)
	print(summation)


if __name__ == '__main__':
	main()