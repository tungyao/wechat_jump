import os,subprocess,time
import threading
class adb:
    def cut_screen(self):
        pipe = subprocess.Popen('adb shell screencap -p /sdcard/screen.jpg',shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # pipe.kill()
        # pipe.wait(2)
        # pipe.kill()
        time.sleep(2)
        pipe.kill()
        print('screenshot is ok')
        self.upload()
    def press(self,time):
        pipe = subprocess.Popen('adb shell',shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        cmd = bytes(('input swipe 400 300 400 500 %d' % time).encode())
        pipe.communicate(input=cmd)
        print('================================')
        print('ok,press time is %dms          |' % time)
        print('================================')
        pipe.kill()
    def upload(self):
        cmd = 'adb pull /sdcard/screen.jpg E:/hub/yum/data/img1.jpg'
        pipe = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        time.sleep(1)
        # pipe.kill()
        print('upload is ok')
if __name__=="__main__":
    a = adb()
    # a.press(650)
    a.cut_screen()