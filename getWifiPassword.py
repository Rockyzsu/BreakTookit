#-*-coding=utf-8-*-
import subprocess

# get system store wifi password

def getwifipassword():
    cmd = 'netsh wlan show profiles'
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    ret   =  p.stdout.readlines()
    profile = [i.split(':')[1].strip() for i in ret if 'All User Profile' in i]
    cmd_pwd = 'netsh wlan show profile {} key=clear'
    ap_password={}
    for ap in profile:
        p = subprocess.Popen(cmd_pwd.format(ap), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        ret = p.stdout.readlines()
        password =  [i.split(':')[1].strip() for i in ret if 'Key Content' in i]
        if not password:
            ap_password[ap]=''
        else:
            ap_password[ap]=password[0]
    return ap_password


print getwifipassword()