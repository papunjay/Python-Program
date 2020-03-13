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
        while temp!=None:
            if( search_data <= temp.data):
                newNode.next=temp
                self.head=newNode
                return

            elif(search_data>=temp.data and temp.next==None):
                temp.next=newNode
                return
            elif(search_data>=temp.data and search_data<=temp.next.data):
                prev=temp
                newNode.next=temp.next
                prev.next=newNode
                return
          
            temp=temp.next

    def search_input(self,search_data):
        if(self.head==None):
            print("LinkList data is empty")
        else:
            temp=self.head
            while temp!=None:
                if(temp.data==search_data):
                    return 1
                temp=temp.next
                if(temp==None):
                    return 0
    def delete_search_data(self,search_data):  
        temp=self.head
        if temp==search_data:
            self.head=temp.next
            temp=None
            return

        else:
            temp=self.head
            while temp!=None:
                if(temp.data==search_data):
                    break
                prev=temp
                temp=temp.next
            prev.next=temp.next
    

list =[]
f=open("file.txt","r")
for word in f.read().split():
    list.append(int(word))
print("your entered data\n{}".format(list))

list=sorted(list)
my_list=LinkList()
for data in list:
    my_list.Insert_Last(data)