class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addRear(self,data):
        self.items.insert(0,data)
string=str(input("Enter the string..."))
result=palChecker(string)
