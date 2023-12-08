from mpi4py import MPI

from master import runMaster
from slave import runSlave
from dotenv import load_dotenv

load_dotenv()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()         # Assign Rank To Every Machine

def run_MPI():

    if rank == 0:              # For Master Machine
        runMaster(comm)

    elif rank > 0:
        runSlave(comm)


if __name__ == "__main__":
    run_MPI()

#  AWS cloudDK  python script to create infrastructure