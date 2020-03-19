import json
class inventoryManagement:
    def __init__(self):
        pass
    
    #read the json file and return the json object 
    def read_file(self):
        file=open("newInventory.json","r")
        data=json.load(file)
        file.close()
        return data
    
    #calculate the total value for every data
    def calculate(self,data):
        print("-----Inventory Details-----")
        for value in data['Inv_details']:
            price = weight=0
            print("name:=",value['name'])
            price+=int(value["price per kg"])
            weight += int(value["weight"])
            print("weight:=",weight)
            print("price:=",price)
            total_price=price*weight
            print("Total_value:=",total_price)
            print("-----Inventory Details-------")

if __name__ == '__main__' :
   invM = inventoryManagement()
   data=invM.read_file()
   invM.calculate(data)