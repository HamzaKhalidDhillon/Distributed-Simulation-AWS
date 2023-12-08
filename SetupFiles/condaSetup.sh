#!/bin/bash

#Download Miniconda from Source For Python3 
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh

#Install Miniconda3 on your machine 
echo -e "\n\nyes\n" | bash Miniconda3-py37_4.10.3-Linux-x86_64.sh > /dev/null 2>&1

#Initializez Conda On your Machine and prompts for restart 
miniconda3/bin/conda init

#Refresh your bashrc to update paths and configure newly installed anaconda
#Tip: Run this file with additional dot for Source to work e.g > . ./yourScript
source ~/.bashrc

