list =[]
f=open("file.txt","r")
for word in f.read().split():
    list.append(int(word))
print("your entered data\n{}".format(list))