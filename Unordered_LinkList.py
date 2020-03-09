'''
'''
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
    def display(self):
        if(self.head==None):
            print("list is empaty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
'''
    def Delete_node(self):
        if(self.data==None):
            print("List id empaty")
        else:
            temp=self.head
            while temp.next.data!==user_data:
                temp=temp.next
            '''
my_list=LinkList()
my_list.Insert_Last(5)
my_list.Insert_Last(8)
my_list.Insert_Last(10)
my_list.Insert_Last(16)
my_list.display()
