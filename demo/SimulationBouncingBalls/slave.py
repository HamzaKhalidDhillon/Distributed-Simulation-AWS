import sys
from pyFmu import Ball_FMU

def runSlave(comm):

    sys.stdout.write("Child is Stimulating.....")
    comm.send("Child Ready",dest=0,tag=1)
    command = comm.recv(source=0,tag=2)
    message= 'error'
    bouncing_fmu = ''

    if(command == "initialize"):
         bouncing_fmu = Ball_FMU()
         print("Slave Initialized")
    comm.send(message, dest=0, tag=3)

    x = bouncing_fmu.getStates()
    while True:

        time = comm.recv(source=0,tag=4)
        if time == '-999':
            break

        bouncing_fmu.update(time=time)
        event_id = bouncing_fmu.getEventIndicator()
        bouncing_fmu.completed_Integrator_Step(event_id)

        comm.send(bouncing_fmu.getStates(), dest=0, tag=5)
        comm.send(bouncing_fmu.getVelocity(), dest=0, tag=6)

        if comm.recv(source = 0,tag = 8)==1:
           temp_x = comm.recv(source = 0, tag = 9)
           temp_y = comm.recv(source = 0, tag = 10)
           bouncing_fmu.setVelocity(temp_x,temp_y)

    bouncing_fmu.finish()
