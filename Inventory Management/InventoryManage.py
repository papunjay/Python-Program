import InventoryFactory  
import Inventory_Data_Management  
cal = Inventory_Data_Management.inventoryManagement()
import json
class createAccount:
    def __init__(self):
        pass 

#read the json file
    def read_file(self):
        file=open("newInventory.json","r")
        data=json.load(file)
        file.close()
        return data

crtA=createAccount()
data=crtA.read_file()
cal.calculate(data)