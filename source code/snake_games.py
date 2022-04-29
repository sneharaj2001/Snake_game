#“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it
from turtle import *

#randrange() method returns a randomly selected element from the specified range.
from random import randrange

#Free Python Games is an Apache2 licensed collection of free Python games
from freegames import square,vector

#inserting 3 elements to play, (i.e) snake,food,aim  - which means creating variables
#vector determines the position(similar to the pointing of graph in maths)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#declaring function
#it is a two dimensional game, so we need two parameters(x,y)
def change(x, y):
    #this two parameters represent the direction of graph
    aim.x = x #it represents the x-axis
    aim.y = y #it represents the y-axis

#declaring another function(inside) to give boundary values
def inside(head):
    return -200 < head.x <190 and -200 < head.y < 190

#declaring anothder function(move) to give movement to the snake
def move():
    #snake moves only in forward direction,so we need to give forward move value(i.e)-1
    #we need to give the copy object, it will copy the same forward value.. so this function will help the snake to move in forward direction 
    head = snake[-1].copy()
    head.move(aim)
    
    #head hits boundary line is out
    #head crosses its own body it is also consider as out
    if not inside(head) or head in snake:
        #if these conditions were satisfied, then the additional red color will be appeared on snake's head
        square(head.x, head.y , 9,'red')
        update()
        return

    #snake.append will add the red color button, when the above condition gets satisfied
    snake.append(head)

    if head == food:
        #if the head of the snake meet the food, it will print the points that scored in the game
        print('snake:',len(snake))
        
        #the below conditions represents, when the snake catches the food and the two variables(x,y) used to show up the next place that the food will appear
        food.x = randrange(-15,15) * 10
        food.y = randrange(-15,15) * 10

    else :
        snake.pop(0) 

    clear()
    
    #snake is the combinations of square
    for body in snake:
        square(body.x,body.y,9,'green')

    square(food.x,food.y,9,'red')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
#tracer bring backs the elements into its initial state
tracer(False)
#listen object is continuously updates the game in every second
listen()

#we need to give controls, so we need to use onkey object
#in onkey, we need to set the controls and give the values(the values are graph values)
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(0,-10),'Down')

move()
done()
        
    
    
    
