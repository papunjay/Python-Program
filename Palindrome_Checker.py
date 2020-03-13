class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addRear(self,data):
        self.items.insert(0,data)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
string=str(input("Enter the string..."))
result=palChecker(string)
