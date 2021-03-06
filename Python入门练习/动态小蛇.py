import turtle
def  drawSnake(rad,angle,len,neckrad):
	for i in range(len):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

	
def main():
	turtle.setup(1300,800,0,0) 
	pythonsize=30
	turtle.pensize(pythonsize)
	turtle.pencolor("blue")
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)
	turtle.pensize(pythonsize)
	turtle.pencolor("green")
	turtle.seth(120)
	drawSnake(40,80,5,pythonsize/2)
	turtle.pensize(pythonsize)
	turtle.pencolor("red")
	turtle.seth(140)
	drawSnake(40,80,5,pythonsize/2)
	turtle.pensize(pythonsize)
	turtle.pencolor("yellow")
	turtle.seth(270)
	drawSnake(40,80,5,pythonsize/2)
	turtle.pensize(pythonsize)
	turtle.pencolor("pink")
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)
	turtle.pensize(pythonsize)
	turtle.pencolor("black")
	turtle.seth(50)
	drawSnake(40,80,5,pythonsize/2)
	


main()

