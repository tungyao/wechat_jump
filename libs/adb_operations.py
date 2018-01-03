import os,subprocess
import threading
class adb:
    def press(self,time):
        pipe = subprocess.Popen('adb shell',shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        cmd = bytes(('input swipe 400 300 400 500 %d' % time).encode())
        pipe.communicate(input=cmd)
        print('ok,press time is %dms' % time)
        pipe.kill()
if __name__=="__main__":
    a = adb()
    a.press(650)