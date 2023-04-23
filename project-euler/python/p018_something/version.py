import random
import turtle


def something():
	turtle.forward(100)
	for i in range(4):
		turtle.left(90)
		if i >= 3:
			turtle.forward(100)
			break
		else:
			turtle.forward(200)
	turtle.done()
		
def main():
	something()

if __name__ == '__main__':
	main()