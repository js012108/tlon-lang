import os
import time

#********Download and install prosody server**********
comando1 = '''
sudo apt-get update
sudo apt-get install prosody
'''
os.system(comando1)
#Give permissions to edit prosody.cfg.lua
comando2 = '''
cd /etc/prosody
sudo chmod 777 prosody.cfg.lua
'''
os.system(comando2)
#read and edit specific line
f = open("/etc/prosody/prosody.cfg.lua", "r")
contents = f.readlines()
f.close()
value = 'admins = { "admin@localhost" } \n'
contents[23] = value
value = 'allow_registration = true \n'
contents[93] = value
value = 'c2s_require_encryption = false \n'
contents[109] = value
value = 's2s_require_encryption = false \n'
contents[115] = value
value = 'VirtualHost "localhost" \n'
contents[204] = value
#saving new prosody.cfg.lua
f = open("/etc/prosody/prosody.cfg.lua", "w")
contents = "".join(contents)
f.write(contents)
f.close()
#*********Start and configure prosody server (admin)*********
#give original permissions to prosody.cfg.lua
comando3 = '''
cd /etc/prosody
sudo chmod 644 prosody.cfg.lua
'''
os.system(comando3)
#give permissions to key and certs of server
comando4 = '''
cd /etc/prosody
sudo chmod 600 certs/localhost.key
sudo chown prosody:prosody certs/localhost.key
sudo chmod 600 certs/localhost.crt
sudo chown prosody:prosody certs/localhost.crt
'''
os.system(comando4)
#finally restart prosody server
comando6 = '''
sudo prosodyctl restart
'''
os.system(comando6)
time.sleep(5)
#register the admin in the 'localhost' host
comando4 = '''
sudo prosodyctl register admin localhost qwertyuiop1
'''
os.system(comando4)
