# D-SimShell-AWS

Framework For Simulating Simulations In a Distributed Manner

# About the Project

This is a sample project to showcase how we can simulate simulations in a distributed manner across a cluster of Machines, We have utilized AWS for providing us a cluster of machines to work on. Some Key Points about the Project

- We have utilized AWS CloudFormation
- AWS ParallelCluster library is utilized to spawn the cluster of EC2 Nodes utilizing AWS Cloud Formation
- OpenMPI standard is uilized however also works for latest versions of Mpich
- Mpi4py pythonic interface built on top of the MPI standards is utilized for all MPI operations 
- pyFmi Library utiized for Loading Simulaions to work on in a python interface 

# Requirements

- Make Sure to Have an AWS Account with necessary privileges(e.g EC2,S3,EBS,VPC)
- Preferably a Linux based Operating System. Newer Vesrions of Parallel Cluster are now supported on Windows too but There are still complications there. You can read about them    in the offiial documentation and make changes according to your OS
-  Latest Version of Python. For this project we utilized python = 3.8.5
-  Miniconda or Anaconda installed to pre-install all requirements for pyFmi 

# Project Structure

Demo contains All the code for running the simulations
## Demo/SimulationBouncingBalls :
 - .env file (Contains Configuration Information For our simulation like the number of machines to work the simulation on and additional properties)
 -  main.py  (The main file that initiates the whole simulation, The file you are supposed to run in your console)
 -  master.py (Contains All the code for The Master Machine like sending and reciving information from the worker machines)
 -  slave.py  (Code for each worker which in our case would represent a Single ball simulation)
 -  Pyfmu.py  (Simple Class for representations of a Ball Object)
 -  animateVisualize.py (After running the Simulation, pass the result file to this program to observe the animation of the whole simulation)
 -  plotVisualize.py (After running the Simulation, pass the result file to this program to observe the plots of the whole simulation)

## Demo/SimulationLorenzFMU : 
 - .env file (Contains Configuration Information For our simulation like the number of machines to work the simulation on and additional properties)
 -  main.py  (The main file that initiates the whole simulation, The file you are supposed to run in your console)
 -  master.py (Contains All the code for The Master Machine like sending and reciving information from the worker machines)
 -  slave.py ----\
 -  slave2.py --------- >These Files Contain the Code for Slave machines which in our case is lorenz components 
 -  slaev3.py ---/
 -  FMU/ (Contain The fmu files for our Simulation)
 
 ## SetupFiles :
 -  Contain The Necessary Scripts to create,configure clusters and setup the project environment on AWS. Will further elaborate how to work these scripts


# Setting Up The Cluster

> ./clusterCreate.sh
- Enter Cluster Name : 

> ./clusterLogin.sh
- Enter Master IP : 
- Enter Master Key Name :

> ./clusterConfig.sh


# How To Run

## Bouncing Balls Simulation

Link : https://drive.google.com/file/d/1qiqRtvCsYvcXetkLGCbkwKMEo2grDdGl/view?usp=sharing

## LorenzFMU

Link : https://drive.google.com/file/d/1sNeqK90Uv-Rw-Ebq062DOuOlWoWQj28F/view?usp=sharing

