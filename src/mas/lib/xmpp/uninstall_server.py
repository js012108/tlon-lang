import os

#********Uninstall prosody server**********
comando1 = '''
sudo apt-get purge --auto-remove prosody
'''
os.system(comando1)
