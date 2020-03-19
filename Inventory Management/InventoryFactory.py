import json 

# function to add to JSON 
def write_json(data, filename='newInventory.json'): 
	with open(filename,'w') as f: 
		json.dump(data, f, indent=4) 

# user input python object to be appended
Name=str(input("Enter the Name:\n"))
Weight=int(input("Enter the Weight:\n"))
price=int(input(" Enter the price \n"))
new_doc={"name":Name,"weight":Weight,"price per kg":price,}
with open('newInventory.json') as json_file: 
	data = json.load(json_file) 
	temp = data['Inv_details'] 	
	
# appending data to emp_details 
	temp.append(new_doc) 
write_json(data) 