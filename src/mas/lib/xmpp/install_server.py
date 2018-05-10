import os
import time

#********Download and install ejabberd 18.01 server**********
comando1 = '''
wget https://www.process-one.net/downloads/downloads-action.php?file=/ejabberd/18.01/ejabberd_18.01-0_amd64.deb
mv downloads-action.php\?file\=%2Fejabberd%2F18.01%2Fejabberd_18.01-0_amd64.deb ejabberd_18.01-0_amd64.deb
sudo dpkg -i ejabberd_18.01-0_amd64.deb
sudo rm ejabberd_18.01-0_amd64.deb
'''
os.system(comando1)

#**********Adding 'tlon' host to ejabberd server**********
#Give permissions to edit ejabberd.yml
comando2 = '''
cd /opt/ejabberd/conf
sudo chmod 777 ejabberd.yml
'''
os.system(comando2)
#read and edit specific line
f = open("/opt/ejabberd/conf/ejabberd.yml", "r")
contents = f.readlines()
f.close()
value = '  - "tlon" \n'
contents[96] = value
#saving new ejabberd.yml
f = open("/opt/ejabberd/conf/ejabberd.yml", "w")
contents = "".join(contents)
f.write(contents)
f.close()

#*********Start and configure ejabberd server (admin)*********
#start server
comando3 = '''
cd /opt/ejabberd-18.01/bin
sudo ./ejabberdctl start
sudo ./ejabberdctl restart
'''
os.system(comando3)
#wait time until the server really starts
time.sleep(15)
#register the admin in the 'tlon' host
comando4 = '''
cd /opt/ejabberd-18.01/bin
sudo ./ejabberdctl register admin tlon qwertyuiop1
'''
os.system(comando4)
#again read ejabberd.yml
f = open("/opt/ejabberd/conf/ejabberd.yml", "r")
contents = f.readlines()
f.close()
#add new line to register admin@tlon as admin account in server and save new file
contents.insert(460,'      - "admin@tlon" ')
f = open("/opt/ejabberd/conf/ejabberd.yml", "w")
contents = "".join(contents)
f.write(contents)
f.close()
#give original permissions to ejabberd.yml
comando5 = '''
cd /opt/ejabberd/conf
sudo chmod 644 ejabberd.yml
'''
os.system(comando5)
#finally restart ejaberd server
comando6 = '''
cd /opt/ejabberd-18.01/bin
sudo ./ejabberdctl restart
'''
os.system(comando6)
