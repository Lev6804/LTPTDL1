import math
class HinhTru_Model:

    def __init__(self, r, h):
        self.r = r
        self.h = h
    
    def area_xq (self):
        return 2*math.pi*self.r*self.h
    
    def area_tp (self):
        return self.area_xq() + 2*math.pi*self.r*self.r
    
    def theTich (self):
        return math.pi * self.r * self.r * self.h
    
    def display (self):
        txt = "{x:.2f}"
        print("Bán Kính: " + txt.format(x=self.r) + "\nChiều cao: " + txt.format(x=self.h) + "\nS xung quang: " + txt.format(x=self.area_xq()) + "\nS toàn phần: " + txt.format(x=self.area_tp()) + "\nThể Tích: " + txt.format(x=self.theTich()) +"\n---------------------")

