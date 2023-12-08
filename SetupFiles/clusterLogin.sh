#!/bin/bash

#MasterIP and Key Required for Logging In the Master Machine 
#Prompt User For Master IP and Key 

echo -ne "Enter Master IP : "

read masterIP

echo -ne "Enter Master Key Name : "

read masterKey


#Copy Required Scripts to the Cluster Master 
scp -i ~/$masterKey condaSetup.sh $masterIP:~/

scp -i ~/$masterKey setupMPI.sh $masterIP:~/

scp -i ~/$masterKey getHosts.sh $masterIP:~/

scp -i ~/$masterKey setupLibs.sh $masterIP:~/

scp -i ~/$masterKey clusterConfig.sh $masterIP:~/

#LogIn to the Master Machine
ssh -i ~/$masterKey $masterIP