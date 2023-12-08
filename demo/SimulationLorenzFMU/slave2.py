from pyfmi import load_fmu
from os import environ

def runSlave2(comm):
    dt = float(environ.get('RATE_OF_CHANGE'))

    response = comm.recv(source=0, tag=1)
    if response == 'Initialize':
        comm.send('Ready', dest=0, tag=2)

    file = comm.recv(source=0, tag=3)

    lorenz_fmuY = load_fmu(file)
    lorenz_fmuY.initialize()

    vref_y = [lorenz_fmuY.get_variable_valueref('x')] + [lorenz_fmuY.get_variable_valueref('y')] + [lorenz_fmuY.get_variable_valueref('z')]

    lorenz_fmuY.time = float(comm.recv(source=0, tag=4))

    print(lorenz_fmuY.time)

    y = lorenz_fmuY.continuous_states


    while True:

        dy = lorenz_fmuY.get_derivatives()

        time = comm.recv(source=0, tag=6)

        if time == '-999':
            break

        lorenz_fmuY.time = time

        y = y + dt*dy

        lorenz_fmuY.continuous_states = y

        comm.send(y, dest=0, tag=5)

        lorenz_fmuY.set_real(vref_y[0], comm.recv(source = 0,tag=8))
        lorenz_fmuY.set_real(vref_y[2], comm.recv(source = 0,tag=9))