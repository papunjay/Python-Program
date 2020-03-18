import json
file=open("Inventory_Management.json","r")
data=json.load(file)
file.close()
print("-----Inventory Details-----")
for value in data:
    
    price=weight=0
    print("Name:=",value['name'])
    price+=int(value["price per kg"])
    weight+=int(value["weight"])
    print("Weight:=",weight)
    print("price:=",price)
    total_price=price*weight
    print("Total_value:=",total_price)
    print("-----Inventory Details-------")
