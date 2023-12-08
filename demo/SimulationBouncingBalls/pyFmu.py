import random
from os import environ

class Ball:
    x = 0
    y = 0
    def __init__(self):
         pass

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y

    def setx(self,x):
        self.x = x

    def sety(self,y):
        self.y = y

class Ball_FMU:

    Ball = '' #(x,y)
    dx = round(random.uniform(-0.5,0.5),4)
    dy = round(random.uniform(-0.5,0.5),4)

    def __init__(self):
        self.width = int(environ.get('WIDTH'))
        self.height = int(environ.get('HEIGHT'))
        self.radius = int(environ.get('RADIUS'))
        self.Ball = Ball()
        self.Ball.setx(random.uniform(self.radius+20, self.height-self.radius))
        self.Ball.sety(random.uniform(self.radius+20, self.width-self.radius))

    def getStates(self):
       return [self.Ball.xcor(),self.Ball.ycor()]

    def getVelocity(self):
        return [self.dx,self.dy]

    def setVelocity(self,x,y):
        self.dx = x
        self.dy = y

    def update(self,time):
         self.Ball.setx(self.Ball.xcor() + self.dx)
         self.Ball.sety(self.Ball.ycor() + self.dy)

    def getDerivative(self):
        return

    def getEventIndicator(self):

        if self.Ball.ycor()-self.radius <= 0:
            #self.dy *= -1
            return 1

        if self.Ball.xcor()-self.radius <= 0:
            #self.dx *= -1
            return 2

        if self.Ball.ycor()+self.radius >= self.height:
            #self.dy *= -1
            return 3

        if self.Ball.xcor()+self.radius >= self.width:
            #self.dx *= -1
            return 4

    def completed_Integrator_Step(self,id):

        if id == 1:
            self.dy *= -1

        if id == 2:
            self.dx *= -1

        if id == 3:
            self.dy *= -1

        if id == 4:
            self.dx *= -1

    def finish(self):
        pass
