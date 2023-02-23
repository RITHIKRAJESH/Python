class coordinates:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,obj):
        return(self.x + obj.x , self.y + obj.y)
obj1=coordinates(55,60)
obj2=coordinates(25,30)
print("sum:",obj1+obj2)
