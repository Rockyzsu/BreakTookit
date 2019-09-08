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
        if self.wifi_connect_status():
            self.logger.info('连接成功')
        else:
            self.logger.info('连接失败')

    def wifi_connect_status(self):
            if self.iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
                return True
            else:
                return False

    def scan(self):
        self.iface.scan()
        time.sleep(3)
        basewifi = self.iface.scan_results()
        for i in basewifi:
            print('wifi 扫描结果：{}'.format(i.ssid))
            print('wifi 对应设备的MAC地址: {}'.format(i.bssid))
            print('='*10)

if __name__ == "__main__":
    wifi = WIFI()
    wifi.scan()