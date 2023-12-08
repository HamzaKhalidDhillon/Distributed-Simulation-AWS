from pyfmi import load_fmu
from os import environ

def runSlave1(comm):
    dt = float(environ.get('RATE_OF_CHANGE'))

    response = comm.recv(source = 0,tag=1)
    if response == 'Initialize':
        comm.send('Ready',dest = 0, tag=2)

    file = comm.recv(source = 0,tag=3)

    lorenz_fmuX = load_fmu(file)
    lorenz_fmuX.initialize()

    vref_x = [lorenz_fmuX.get_variable_valueref('x')] + [lorenz_fmuX.get_variable_valueref('y')]

    lorenz_fmuX.time = comm.recv(source = 0,tag=4)

    print(lorenz_fmuX.time)

    x = lorenz_fmuX.continuous_states


    while True:

        dx = lorenz_fmuX.get_derivatives()

        time = comm.recv(source=0,tag=6)

        if time == '-999':
            break

        lorenz_fmuX.time = time

        x = x + dt*dx

        lorenz_fmuX.continuous_states = x

        comm.send(x, dest=0, tag=5)

        lorenz_fmuX.set_real(vref_x[1], comm.recv(source = 0,tag=7))



################################################################################################################################


###########################################################################################################################


