import numpy as np
class calcula:
    LENGTH = None
    PRESS_TIME =None
    POINT =None
    POINTs =None
    def get_point(self):
        width = np.abs(self.POINT[0] -self.POINTs[0])
        heigth = np.abs(self.POINT[1]- self.POINTs[1])
        a = np.sqrt(width**2+heigth**2)

        return int(a)
    def value(self):
        print("INFO LENGTH is ",self.get_point())
        a =(self.get_point()/8)*18+135
        print("INFO calculate time is %dms"%a)
        return int(a)
if __name__ =="__main__":
    a = calcula()
    a.LENGTH =235
    a.POINT = [155,509]
    a.POINTs = [357,388]
    a.value()