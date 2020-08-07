import turtle

turtle.title ("my turtle game")
turtle.bgcolor("black")
turtle.setup(600,600)

screen = turtle.Screen()
bob = turtle.Turtle()
bob.color("white")
bob.speed(0)
bob.pensize(3)
bob.shape("turtle")
sides = 5

def spiral(angle, increase):
  steps = 5
  for i in range(500):
    bob.forward(steps)
    bob.left(angle)
    steps += increase
  

spiral(angle = 360/sides+1 ,increase=1 )