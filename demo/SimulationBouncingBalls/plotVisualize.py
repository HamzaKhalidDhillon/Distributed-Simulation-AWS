import pandas as pd
import turtle
import pylab as P
from os import environ
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
df = pd.read_csv('result.txt',delimiter=',')


numOfSlaves = int(environ.get('NUM_OF_SLAVES'))

width = int(environ.get('WIDTH'))
height = int(environ.get('HEIGHT'))

T_END = int(environ.get('TIME_END'))

time = df['time']

for i in range(1,T_END,500):
    plt.figure(figsize=(1000,1000))
    for j in range(1,numOfSlaves+1):
        plt.scatter(df['ball{x}_x'.format(x=j)][i],df['ball{y}_y'.format(y=j)][i],c=1,s=200)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Bouncing Ball Simulation")
    plt.show()
