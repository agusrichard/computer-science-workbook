import random

def the_birthday_problem(reps=100):
	reps_result = []
	for i in range(reps):
		birthdays = []
		while True:
			x = random.randrange(0, 365)
			if x in birthdays:
				break
				print("Runned")
			else:
				birthdays.append(x)
		reps_result.append(len(birthdays))
	return reps_result, sum(reps_result) / len(reps_result)


def main():
	result, average = the_birthday_problem()
	print(result)
	print("Average: ", average)


if __name__ == '__main__':
	main()
