import pandas as pd
from os import environ
import turtle
import pylab as P
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

colors = ["green","blue","red","purple","white","yellow"]

df = pd.read_csv('result.txt',delimiter=',')

T_START = int(float(environ.get('TIME_START')))
T_END = int(environ.get('TIME_END'))

numOfSlaves = int(environ.get('NUM_OF_SLAVES'))

width = int(environ.get('WIDTH'))
height = int(environ.get('HEIGHT'))

wn = turtle.Screen()
wn.screensize(canvwidth=width, canvheight=height)
wn.setup(width=width, height=height)

wn.bgcolor("black")
wn.title("Ball Simulation")
wn.tracer(0)

turtleList = []

for i in range(0,numOfSlaves):
    turtleObj = turtle.Turtle()
    turtleObj.shape('circle')
    turtleObj.color(colors[i%6])
    turtleObj.penup()
    turtleList.append(turtleObj)

for i in range(T_START,T_END):
    for index,obj in enumerate(turtleList):
        obj.setx(df[df.columns[index*2+1]][i]-int(height/2))
        obj.sety(df[df.columns[index*2+2]][i]-int(width/2))
    wn.update()

turtle.bye()