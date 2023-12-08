#!/bin/bash

echo -ne "Enter Cluster Name : "
read name

pcluster create $name