import numpy as np
class calcula:
    LENGTH = None
    PRESS_TIME =None
    def run(self):
        a = self.LENGTH*0.4*self.LENGTH*1.35
        print("INFO calculate time is %dms"%a)
        return int(a)
if __name__ =="__main__":
    a = calcula()
    a.LENGTH =35
    a.run()