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
        if self.head is None:
            print("the list is empty")
            return
        else:
            temp=self.head
            while temp is not None:
                if temp.data==search_data:
                    return 1
                temp = temp.next
                if temp==None:
                    return 0
    def Delete_node(self,search_data):
        temp=self.head
        if(temp.data==search_data):
            self.head=temp.next
            temp=None
            return
        else:
            while(temp is not None):
                if temp.data==search_data:
                    break
                prev=temp
                temp=temp.next
            prev.next =temp.next
    def link_list_to_list(self):
        temp=self.head
        list=[]  
        while(temp is not None):
            list.append(temp.data)
            temp=temp.next
        return list

f = open('new_file.txt', 'r')
my_list=LinkList()
for word in f.read().split():
    my_list.Insert_Last(word)

print("Your Entered data is...")
my_list.display()

search_data=str(input("Enter the data for search...   "))
result=my_list.Search_linkList(search_data)
if(result==0):
   my_list.Insert_Last(search_data)
else:
    my_list.Delete_node(search_data)

string_data=my_list.link_list_to_list()
write_file=open("new_file.txt","w")
str1=" "
write_file.write(str1.join(string_data))
