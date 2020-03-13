class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None  

    def Insert_Last(self,value):
        newNode=node(value)
        if(self.head==None):
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode 
              
    def Insert_at_position(self,search_data):
        newNode=node(search_data)
        temp=self.head
        prev=None

   
list =[]
f=open("file.txt","r")
for word in f.read().split():
    list.append(int(word))
print("your entered data\n{}".format(list))

list=sorted(list)
my_list=LinkList()
for data in list:
    my_list.Insert_Last(data)