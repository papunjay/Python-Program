class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode

    def isempty(self):
        if self.head==None:
            return True
        else:
            return False

    def pop(self):
        if self.isempty():
            return None
        else:
            pop_head=self.head
            self.head=self.head.next
            pop_head=None
    def display(self):
        temp =self.head
        if self.isempty():
            print("Stack is empty")
        else:
            while(temp!=Node):
                print(temp.data)
                temp=temp.next
            return
class anagramNumber:
   
    def prime_fun(self,Number_range):
        prime_data=[]
        for Number in range(2,Number_range+1):
            checker=0
            for divider in range(1,Number):
                if(Number%divider==0):
                    checker+=1
            if(checker==1):
                prime_data.append(Number)
        return prime_data

    def check_anagram(self,prime_list):
        ana_list=[]
        for ith in prime_list:
            dist=0
            for jth in prime_list:
                if((ith!=jth )and (sorted(str(ith))==sorted(str(jth)))):
                    for index in range(len(ana_list)):
                        if(ith==ana_list[index]):
                            dist+=1
                    if(dist==0):
                        ana_list.append(int(ith))
        return ana_list
Number_range=1000
myStack=Stack()
anaOb=anagramNumber()
prime_list=anaOb.prime_fun(Number_range)
ana_list=anaOb.check_anagram(prime_list)
for ana in ana_list:
    myStack.push(ana)

myStack.display()