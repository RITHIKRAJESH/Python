import datetime
    
class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,obj):
        return datetime.timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)+ datetime.timedelta(hours=obj.hour,minutes=obj.minute,seconds=obj.second)
obj1=time(1,20,34)
obj2=time(3,24,10)
print(obj1+obj2)
