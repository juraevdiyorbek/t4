class Date:
    def __init__(self,day :int,month:int,year:int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def getDay(self):
        return  f"%02d" %(self.day)
    def getMonth(self):
        return   f"%02d" %(self.month)       
    def getYear(self):
        return self.year
    def setDay(self,newDay):
        self.day = newDay
    def setMonth(self,newMonth):
        self.month= newMonth
    def setYear(self,newyear):
        self.year = newyear
    def setDate(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def toString(self):
        return f"%02d/%02d/%0002d" %(self.day,self.month,self.year)
    
data = Date(13,1,1982)
print(data.toString())

# print(data.getDay())
# print(data.getMonth())
# data.setDay(20)
# print(data.getDay())
data.setDate(20,6,1982)
print(data.toString())