# 扫描wifi
import time
from pywifi import const
import pywifi
from Base import BaseServices
class WIFI(BaseServices):

    def __init__(self):
        self.logger = self.get_lloger()
        self.wifi=pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]

    def start(self):
        username='printer'
        password='zxcvbnm0'
        basewifi = self.scan()

        for i in basewifi:
            print('wifi 扫描结果：{}'.format(i.ssid))
            print('wifi 对应设备的MAC地址: {}'.format(i.bssid))
            print('='*10)

            

    def wifi_connect_status(self):
            if self.iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
                return True
            else:
                return False

    def scan(self):
        self.iface.scan()
        time.sleep(3)
        basewifi = self.iface.scan_results()
        return basewifi

    def connect(self,ssid,password,sleep_time=3):
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

        if self.wifi_connect_status:

            self.logger.info(f'{ssid} 连接成功')
            self.logger.info(f'{ssid}的密码是{password}')
            return True

        else:
            # print('连接失败')
            return False

    def disconnect(self,sleep_time):
        self.iface.disconnect()
        time.sleep(sleep_time)

if __name__ == "__main__":
    wifi = WIFI()
    # wifi.scan()
    wifi.disconnect()
    wifi.connect()