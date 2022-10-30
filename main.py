import random
import turtle as t

#TODO1 Extract Colors using Colorgram or create random color list
colorsList = []
def randomColor():
  for x in range(10):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colorsList.append((r, g, b))


#Runs color function
randomColor()
#print(colorsList)

#Create Turtle and set color mode
#Also sets screensize in coordinates
henry = t.Turtle()
screen = t.Screen()
screen.setworldcoordinates(-50,-7.5,50,7.5)
t.colormode(255)
henry.speed("fastest")

#Turtle starting at bottom right 
henry.penup()
henry.goto(-50, -7)
henry.pendown()
#henrys original position
#starting = ()

#Finds henrys position and adds 1 to y and returns new starting position
def startCoords():
  '''Finds henrys position and adds 1 to y and returns new starting position'''
  newCoords = henry.pos()
  new_y = int(newCoords[1])
  return (-50, new_y + 1)

#Brings henry back to left of page to start again
def restartHenry():
  '''Brings henry back to left of page to start again'''
  henry.penup()
  henry.goto(startCoords())
  henry.pendown()

#Function to create dot
def createDot():
  '''Function to create dot'''
  henry.color(random.choice(colorsList))
  henry.dot()
  henry.penup()
  henry.forward(4)
  henry.pendown()

#Finds coordinates of henry and returns if henry hit right wall
def hitWall():
  '''Finds coordinates of henry and returns if henry hit right wall (x axis ends)'''
  position = henry.pos()
  if int(position[0]) >= 50:
    return True
  else:
    return False

#Finds coordinates of henry and returns if henry hit ceiling
def hitCeiling():
  '''Finds coordinates of henry and returns if henry hit ceiling (y axis ends)'''
  position = henry.pos()
  if int(position[1]) >= 7.5:
    return True
  else:
    return False

#henry dot walk
while not hitCeiling():
  if not hitWall(): 
    createDot()
  else:
    restartHenry()


#TODO4 Allow turtle to pick random colors and create dot


#TODO5 Have turtle evenly go across page horizontally and verically placing dots



screen.exitonclick