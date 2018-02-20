#!/bin/bash

sudo modprobe ipv6
sudo sleep 2
sudo modprobe batman-adv
sudo ifconfig wlan0 down
sudo ifconfig eth0 down
sudo iwconfig wlan0 mode ad-hoc
sudo ifconfig wlan0 mtu 1532
sudo iwconfig wlan0 mode ad-hoc essid TLON-ADHOC ap 02:1B:55:AD:0C:02 channel 1
sudo sleep 1

sudo batctl if add wlan0
sleep 1
sudo ip link set up dev wlan0
sudo ifconfig eth0 0.0.0.0 up
sudo ip link add name tlon0 type bridge
sudo ip link set dev eth0 master tlon0
sudo ip link set dev bat0 master tlon0
#sudo ifconfig tlon0 inet6 add fe80::a00:3/64  



ip6_bat0=$(ifconfig tlon0 |egrep -o '([[:xdigit:]]{2}[:]){5}[[:xdigit:]]{2}')
ip6_wlan0=$(ifconfig wlan0 |egrep -o '([[:xdigit:]]{2}[:]){5}[[:xdigit:]]{2}')

function mac_2_ip()
        {
        IFS=':'; set ${1,,}; unset IFS
        echo "fe80::$(printf %02x $((0x$1 ^ 2)))$2:${3}ff:fe$4:$5$6"
        }

var2=$(mac_2_ip $ip6_bat0)
var3=$(mac_2_ip $ip6_wlan0)
sudo ifconfig tlon0 inet6 add $var2/64
sudo ifconfig tlon0 inet6 add $var3/64
sudo ifconfig bat0 0.0.0.0 up
#sudo ifconfig tlon0 192.168.2.3 up
sleep 2
sudo alfred -i tlon0 -m > /dev/null&

