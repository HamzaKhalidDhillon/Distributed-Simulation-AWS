#!/bin/bash

#Store Master IP in a hostfile
hostname -I | awk '{print $1}' >> ~/hostfile 
qhost > slaveIPs.txt
#Store All Slave Machine IP's in a hostfile
cat slaveIPs.txt | grep 'ip-' |  cut -c 1-20 >> ~/hostfile

rm slaveIPs.txt
