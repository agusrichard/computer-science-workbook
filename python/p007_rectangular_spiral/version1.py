import turtle

turtle.speed('fastest')

def rectangular_pyramid(walk=10, difference=2, length=250):
	if walk > length:
		return
	for i in range(4):
		turtle.pendown()
		turtle.forward(walk)
		turtle.left(90)
	turtle.penup()
	turtle.backward(difference)
	turtle.right(90)
	turtle.forward(difference)
	turtle.left(90)
	rectangular_pyramid(walk+2*difference)

def main():
	rectangular_pyramid()

if __name__ == '__main__':
	main()