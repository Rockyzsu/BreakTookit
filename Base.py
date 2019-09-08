import logging
import time

class BaseServices(object):

    def get_lloger(self,filename='default.log'):
        logger = logging.getLogger(filename)  # 不加名称设置root logger

        logger.setLevel(logging.DEBUG) # 设置输出级别

        formatter = logging.Formatter(
            '[%(asctime)s][%(filename)s][line: %(lineno)d]\[%(levelname)s] ## %(message)s)',
            datefmt='%Y-%m-%d %H:%M:%S')

        # 使用FileHandler输出到文件
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # 使用StreamHandler输出到屏幕
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        # 添加两个Handler
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
