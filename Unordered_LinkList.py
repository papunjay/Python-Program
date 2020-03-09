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
    def Search_linkList(self,search_data):
        temp=self.head
        while(temp.next!=None or temp.data==search_data):
            temp=temp.next
        if(temp.next==None):
            return 1
        else:
            return 0
'''
    def Delete_node(self):
        if(self.data==None):
            print("List id empaty")
        else:
            temp=self.head
            while temp.next.data!==user_data:
                temp=temp.next
            '''
str1=[]
f = open('new_file.txt', 'r')
str1=f.read().split()
my_list=LinkList()
for word in str1:
    my_list.Insert_Last(word)
print("Your Entered data is...")
my_list.display()
search_data=str(input("Enter the data for search"))
result=my_list.Search_linkList(search_data)
print(result)
if(result==1):
   my_list.Insert_Last(search_data)
   
my_list.display()

