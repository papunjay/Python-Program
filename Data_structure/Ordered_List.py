class node:
    def __init__(self,data):
        self.data=data
        self.next=None
list =[]
f=open("file.txt","r")
for word in f.read().split():
    list.append(int(word))
print("your entered data\n{}".format(list))

list=sorted(list)
my_list=LinkList()
for data in list:
    my_list.Insert_Last(data)