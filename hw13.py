import turtle, math, random
class Lander(turtle.Turtle):
  '''
Purpose:  The lander which is a character in the game which is a turtle object
Instance variables:  start_dx, start_dy, start_vx, start_vy, which rep. the (x,y) and velocity in x and y direction of the start of the lander
Methods: init() which initializes variables, move() which changes the landers position, thrust() which is for an up button event, moves the lander up, turnright() and turnleft() is to turn the lander direction
  '''
  def __init__(self, start_dx, start_dy, start_vx, start_vy):
     turtle.Turtle.__init__(self)
     self.vx = start_vx
     self.vy = start_vy
     self.fuel = 50
     self.left(90)
     self.penup()
     self.setpos(start_dx, start_dy)
     self.speed(0)

     self.color('blue')
  def move(self):
     self.vy = self.vy - 0.0486
     self.dx = self.xcor()+self.vx
     self.dy = self.ycor()+self.vy
     self.setpos(self.dx,self.dy)
  def thrust(self):
     print('Up button pressed')
     if self.fuel >= 0:
       self.fuel-=1
       theta = math.radians(self.heading())
       self.thrust_vx = math.cos(theta)
       self.thrust_vy = math.radians(math.sin(theta))
       self.vx += self.thrust_vx
       self.vy = self.thrust_vy
       self.move()
       print(self.fuel)
     else:
       print('Out of fuel')
  def turnright(self):
      print('Right button pressed')
      if self.fuel > 0:
         self.fuel-=1
         self.right(10)
         print(self.fuel)
      else:
         print('Out of fuel')
  def turnleft(self):
      print('Left button pressed')
      if self.fuel > 0:
         self.fuel-=1
         self.left(10)
         print(self.fuel)
      else:
         print('Out of fuel')



class Game:
  '''
Purpose: (What does an object of this class represent?) the game, putting everything together to create the turtle window and have our objects displayed in it
Instance variables: (What are the instance variables for this class,
and what does each represent in a few words?) just self which is an instance of the object itself
Methods: (What methods does this class have, and what does each do in a few words?) __init__() which initializes variables, and gameloop() which updates the turtle screen, also spawns and moves the meteors, assign events to functions, keeps the game running
'''
  def __init__(self):
    turtle.setworldcoordinates(0, 0, 1000, 1000)
    turtle.delay(0)
    self.player = Lander(random.uniform(100,900), random.uniform(500,900),random.uniform(-5,5),random.uniform(0,-5))
    self.boo = True
    self.lst = []

    self.player.turtlesize(2)
    self.gameloop()
    turtle.onkeypress(self.player.thrust, 'Up')
    turtle.onkeypress(self.player.turnright, 'Right')
    turtle.onkeypress(self.player.turnleft, 'Left')
    turtle.listen()
    turtle.mainloop()

  def gameloop(self):
      if self.player.ycor() >= 10 and self.boo == True:
         self.player.move()
         num = random.randint(1,5)
         if num == 3:
            self.lst.append(Meteor(random.uniform(10,990), 1000,0,0))
         for i in self.lst:
             i.move()
             dist = math.sqrt(((i.xcor()-self.player.dx)**2) + (i.ycor()-self.player.dy)**2)
             if dist < 25:
                self.boo = False
                print('You crashed!')

         turtle.Screen().ontimer(self.gameloop, 30)
      elif self.player.ycor() < 10 and self.boo == True:
          if self.player.vx > 3 or self.player.vy > 3:
             print('You crashed!')
          else:
             print('Successful landing!')





class Meteor(turtle.Turtle):
  '''
Purpose: (What does an object of this class represent?) a meteor objects
Instance variables: (What are the instance variables for this class,
and what does each represent in a few words?) same as lander, start_dx, start_dy, start_vx, start_vy, which rep. the (x,y) and velocity in x and y direction of the start of the meteor
Methods: (What methods does this class have, and what does each do in a few words?) same as lander, init() which initializes variables, move() which changes the meteors position
  '''
  def __init__(self, start_dx, start_dy, start_vx, start_vy):
     turtle.Turtle.__init__(self)
     self.vx = start_vx
     self.vy = start_vy
     self.fuel = 50
     self.left(90)
     self.penup()
     self.setpos(start_dx, start_dy)
     self.speed(0)
     self.shape('circle')
     self.color('red')

     turtle.Screen().bgcolor('yellow')

  def move(self):
     self.vy = self.vy - 0.0486
     self.dx = self.xcor()+self.vx
     self.dy = self.ycor()+self.vy
     self.setpos(self.dx,self.dy)



Game()
