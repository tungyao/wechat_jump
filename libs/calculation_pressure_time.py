import numpy as np
class calcula:
    LENGTH = None
    PRESS_TIME =None
    def run(self):
        a =(self.LENGTH+1)*1.36535*14
        print("INFO calculate time is %dms"%a)
        return int(a)
if __name__ =="__main__":
    a = calcula()
    a.LENGTH =40
    a.run()