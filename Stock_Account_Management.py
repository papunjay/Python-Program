import json
file=open("Stock_Account_Management.json","r")
stack_details=json.load(file)
file.close()
N=int(input("Enter the number of stock..."))
print("\n")
 
for value in stack_details:
    total_value=0 
    print("Stock Name:",value['Stock Names'])
    print("Number of Share",value['Number of Share'])
    print("Share Price",value['Share Price'])
    no_of_share=int(value['Number of Share'])
    share_price=int(value['Share Price'])
    total_value=no_of_share*share_price
    print("Total",total_value)
    print("\n")
 