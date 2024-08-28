

class Rectangle:

    def __init__ (self, width, length):
        self.width = width
        self.length = length

    def area (self):
        return self.width*self.length
    
    def perimeter (self):
        return (self.width + self.length)*2
    
    def display (self):
        print("Rộng: " + str(self.width) + " Dài: " + str(self.length) + " Area: " + str(self.area()) + " Perimeter: " + str(self.perimeter()))