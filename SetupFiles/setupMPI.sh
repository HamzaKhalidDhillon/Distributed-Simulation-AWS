#!/bin/bash

#Download MPI4PY from Source
wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-3.0.3.tar.gz

tar -zxf mpi4py-3.0.3.tar.gz

cd mpi4py-3.0.3

#Create Build For MPI4PY 
python setup.py build

#Install MPI4PY On your Machine 
python setup.py install