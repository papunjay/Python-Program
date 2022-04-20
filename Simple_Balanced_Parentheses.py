class Balanced_Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if s.is_empty():
            self.items=False
        else:
            self.items.pop()
s=Balanced_Stack()
expresion=str(input("Enter the Expretion...."))
for exp in expresion:
    if(exp =='('):
        s.push(exp)
    elif(exp == ')'):
        s.pop()
result=s.is_empty()
print(result)
if result==True:
    print("balanced")
else:
    print("unbalanced")