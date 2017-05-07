import time
import os

def shutdown(seconds):
    time.sleep(seconds)
    os.system("shutdown -s -t 0")

if __name__ == '__main__':
    seconds = 300
    shutdown(seconds)