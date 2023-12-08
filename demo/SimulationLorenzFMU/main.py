from mpi4py import MPI

from master import runMaster
from slave import runSlave1
from slave2 import runSlave2
from slave3 import runSlave3
from dotenv import load_dotenv
load_dotenv()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

bouncing_fmu = None

def run_MPI():

    if rank == 0:
        runMaster(comm)

    elif rank == 1:
        runSlave1(comm)

    elif rank == 2:
        runSlave2(comm)

    elif rank == 3:
        runSlave3(comm)

if __name__ == "__main__":
    run_MPI()

#  AWS cloudDK  python script to create infrastructure