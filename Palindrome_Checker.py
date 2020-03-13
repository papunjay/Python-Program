class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
string=str(input("Enter the string..."))
result=palChecker(string)
