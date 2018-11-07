import os

#********Uninstall ejabberd 18.01 server**********
comando1 = '''
sudo apt-get remove --purge ejabberd
cd /opt/
sudo rm -rf ejabberd/
sudo rm -rf ejabberd-18.01/
'''
os.system(comando1)