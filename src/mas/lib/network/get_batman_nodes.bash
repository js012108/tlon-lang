#! /bin/bash
var1=$(sudo batctl o |sed '1,2 d'|grep -oiE '([0-9A-F]{2}:){5}[0-9A-F]{2}'|sort|uniq;)
echo $var1
var2=$(sudo batctl o |grep -oiE '([0-9]+[.][0-9]+)'|sed '1 d' |sort|uniq)
echo $var2


