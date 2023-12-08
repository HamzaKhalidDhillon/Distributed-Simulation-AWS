from pyfmi import load_fmu
from os import environ

def runSlave3(comm):
    dt = float(environ.get('RATE_OF_CHANGE'))

    response = comm.recv(source=0, tag=1)
    if response == 'Initialize':
        comm.send('Ready', dest=0, tag=2)

    file = comm.recv(source=0, tag=3)

    lorenz_fmuZ = load_fmu(file)
    lorenz_fmuZ.initialize()

    vref_z = [lorenz_fmuZ.get_variable_valueref('x')] + [lorenz_fmuZ.get_variable_valueref('y')] + [ lorenz_fmuZ.get_variable_valueref('z')]

    lorenz_fmuZ.time = comm.recv(source=0, tag=4)

    print(lorenz_fmuZ.time)

    z = lorenz_fmuZ.continuous_states


    while True:

        dz = lorenz_fmuZ.get_derivatives()

        time = comm.recv(source=0, tag=6)

        if time == '-999':
            break

        lorenz_fmuZ.time = time

        z = z + dt*dz

        lorenz_fmuZ.continuous_states = z

        comm.send(z, dest=0, tag=5)

        lorenz_fmuZ.set_real(vref_z[0], comm.recv(source = 0,tag=10))
        lorenz_fmuZ.set_real(vref_z[1], comm.recv(source = 0,tag=11))