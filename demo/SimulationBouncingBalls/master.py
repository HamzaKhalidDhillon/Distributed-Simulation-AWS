import math
from os import environ

def checkEvent(sol,vel):
   radius = int(environ.get('RADIUS'))
   numOfSlaves = int(environ.get('NUM_OF_SLAVES'))
   events = {}

   for i in range(1,numOfSlaves+1):
       events[i]=0
   for i in range(1,numOfSlaves):
       for j in range(i+1,numOfSlaves+1):
          if (math.sqrt((sol[i][-1][0] - sol[j][-1][0]) ** 2
                                           + (sol[i][-1][1] - sol[j][-1][1]) ** 2)) < radius:
                  events[i] = vel[j]
                  events[j] = vel[i]
   return events

def runMaster(comm):
    numOfSlaves = int (environ.get('NUM_OF_SLAVES'))

    for i in range(numOfSlaves):
        message = comm.recv(source=i+1, tag=1)
        comm.send("initialize",dest=i+1,tag=2)
        message = comm.recv(source=i+1, tag=3)

    Tstart = float(environ.get('TIME_START'))  # The start time.
    Tend = float(environ.get('TIME_END'))  # End time

    time = Tstart
    dt = float(environ.get('STEP_SIZE'))

    t_sol = {}
    t_time = []

    t_vel = {}

    count = 0

    while time < Tend:
        time = time + dt
        for i in range(1,numOfSlaves+1):
            comm.send(time,dest=i,tag = 4)
        for i in range(1,numOfSlaves+1):
            #rec = comm.recv(source=i,tag = 5)
            if i in t_sol:
               t_sol[i].append(comm.recv(source=i,tag = 5))
            else:
                t_sol[i] = []
                t_sol[i].append(comm.recv(source=i, tag=5))
            t_vel[i] = comm.recv(source=i,tag=6)

        events = checkEvent(t_sol,t_vel)

        for i in range(1,numOfSlaves+1):
            if(events[i]==0):
                comm.send(-1,dest=i ,tag = 8)
            else:
                count += 1
                comm.send(1,dest=i ,tag = 8)
                comm.send(events[i][0],dest=i, tag = 9)      #dx
                comm.send(events[i][1],dest=i, tag = 10)     #dy

        t_time.append(time)

    for i in range(1,numOfSlaves+1):
        comm.send('-999', dest=i, tag=4)

    ResultToFile(t_time,t_sol)

def ResultToFile(t_time,t_sol):
    numOfSlaves = int(environ.get('NUM_OF_SLAVES'))
    with open('result.txt','w') as file:
         file.write('time')
         for i in range(1,numOfSlaves+1):
               file.write(',ball{x}_x'.format(x=i))
               file.write(',ball{x}_y'.format(x=i))
         for index,time in enumerate(t_time):
             file.write('\n')
             file.write(str(round(time,2)))
             for i in range(1,numOfSlaves+1):
                 file.write(','+str(round(t_sol[i][index][0],2)))
                 file.write(',' + str(round(t_sol[i][index][1], 2)))



