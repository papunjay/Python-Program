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
    def size(self):
        return len(self.items)
def palChecker(string):
    chardeque=Deque()
    for ch in string:
        chardeque.addRear(ch)
    check=True
    while chardeque.size() > 1 and check:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            check=False
    return check
        
string=str(input("Enter the string..."))
result=palChecker(string)
