import os
import time

#********Download and install ejabberd 18.01 server**********
comando1 = '''
sudo apt-get -y install ejabberd
sudo chmod 777 -R /etc/ejabberd
sudo chmod 777 /etc/ejabberd/ejabberd.yml
'''
os.system(comando1)

#**********Adding 'tlon' host to ejabberd server**********
#Give permissions to edit ejabberd.yml
comando2 = '''
/etc/ejabberd
'''
os.system(comando2)
#read and edit specific line
f = open("/etc/ejabberd/ejabberd.yml", "r")
contents = f.readlines()
f.close()
value = '  - "tlon" \n'
contents[83] = value
#saving new ejabberd.yml
f = open("/etc/ejabberd/ejabberd.yml", "w")
contents = "".join(contents)
f.write(contents)
f.close()

#*********Start and configure ejabberd server (admin)*********
#start server
comando3 = '''
sudo ejabberdctl start
sudo ejabberdctl restart
'''
os.system(comando3)
#wait time until the server really starts
time.sleep(15)
#register the admin in the 'tlon' host
comando4 = '''
sudo ejabberdctl register admin tlon qwertyuiop1
'''
os.system(comando4)
#again read ejabberd.yml
f = open("/etc/ejabberd/ejabberd.yml", "r")
contents = f.readlines()
f.close()
#add new line to register admin@tlon as admin account in server and save new file
contents.insert(418,'       - "admin@tlon" \n ')
f = open("/etc/ejabberd/ejabberd.yml", "w")
contents = "".join(contents)
f.write(contents)
f.close()
#finally restart ejaberd server
comando5 = '''
sudo ejabberdctl restart
'''
os.system(comando5)
