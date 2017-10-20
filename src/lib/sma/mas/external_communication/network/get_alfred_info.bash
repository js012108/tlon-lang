#!/bin/bash

# To use this script it is necesary to modify visudo file and
# allow the user use sudo without password

sudo su <<HERE
alfred -r $1
exit
HERE
