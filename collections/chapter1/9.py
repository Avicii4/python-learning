from time import sleep
from datetime import datetime

if __name__ == '__main__':
    for i in range(60):
        now = datetime.now()
        print('当前北京时间：' + now.strftime('%H:%M:%S'))
        sleep(1)
