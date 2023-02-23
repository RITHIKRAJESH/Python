class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        print("perimeter:",2*(self.length+self.breadth))
    def area(self):
        print("area:",self.length*self.breadth)
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
rec1=rectangle(l,b)
rec1.area()
rec1.perimeter()
