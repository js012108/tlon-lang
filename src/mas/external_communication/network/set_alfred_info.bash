#!/bin/bash

# To use this script it is necesary to modify visudo file and
# allow the user use sudo without password

sudo su <<HERE
echo $1 | alfred -s $2
echo $1
echo $2
exit
HERE

