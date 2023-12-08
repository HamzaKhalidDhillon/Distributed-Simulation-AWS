import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from os import environ

def runMaster(comm):

    noOfSlaves = int(environ.get('NUM_OF_SLAVES'))
    fmu_path = environ.get('FMU_PATH')

    fmi_scripts = ['LorenzX.fmu','LorenzY.fmu','LorenzZ.fmu']

    for index in range(noOfSlaves):
        comm.send('Initialize',dest = index+1, tag = 1)
        response = comm.recv(source = index+1, tag = 2)

    for index,file in enumerate(fmi_scripts):
        print(file,' ',index)
        comm.send(fmu_path+file,dest = index+1,tag = 3)

# -------------------------------------------------------------------- #

    timeStart = float(environ.get('TIME_START'))
    timeEnd = float(environ.get('TIME_END'))
    dt = float(environ.get('RATE_OF_CHANGE'))

    time = timeStart

    for i in range(noOfSlaves):
        comm.send(timeStart,dest = i+1, tag = 4)

    t_time = []
    t_sol = {'X': [], 'Y': [], 'Z': []}



    while time < timeEnd:

        time = time + dt

        for i in range(noOfSlaves):
            comm.send(time,dest = i+1,tag=6)

        x = round(float(comm.recv(source=1, tag=5)), 2)
        y = round(float(comm.recv(source=2, tag=5)), 2)
        z = round(float(comm.recv(source=3, tag=5)), 2)

        comm.send(y,dest = 1,tag = 7)

        comm.send(x,dest = 2,tag = 8)
        comm.send(z,dest = 2,tag = 9)

        comm.send(x, dest=3, tag=10)
        comm.send(y, dest=3, tag=11)

        t_time.append(time)
        t_sol['X'].append(list([x,y]))
        t_sol['Y'].append(list([x,y,z]))
        t_sol['Z'].append(list([x,y,z]))

    for i in range(noOfSlaves):
        comm.send('-999', dest=i + 1, tag=6)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    Sol_X = np.array(t_sol['X'])
    Sol_Y = np.array(t_sol['Y'])
    Sol_Z = np.array(t_sol['Z'])

    ax.scatter(Sol_X[:, 0], Sol_X[:, 1], marker='.')
    ax.scatter(Sol_Y[:, 0], Sol_Y[:, 1], Sol_Y[:, 2], marker='.')
    ax.scatter(Sol_Z[:, 0], Sol_Z[:, 1], Sol_Z[:, 2], marker='.')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.rcParams['figure.figsize'] = [220, 220]
    plt.show()






