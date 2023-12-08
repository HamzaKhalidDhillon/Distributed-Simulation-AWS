#!/bin/bash

echo -ne "Enter Cluster Name : "
read name

pcluster delete $name