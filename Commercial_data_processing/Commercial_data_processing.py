class StockAccount:
    def Create_new_Acc(self):
        f = open("newUser.json","a+")
        name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))
        phno = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        cont = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(Age)+'",\n'+'       "Ph.No" : "'+str(phno)+'",\n'+'"Share Amount" : "'+str(amount)+'" }]')
        print("The Data has been Stored Successfully in 'newUser.json' file. ") 

    def File_Input(self):

stAcc=StockAccount()
if __name__ == '__main__':
    inp = input(" Are You having an Existing Account? (y/n):")
    
    if (inp == "y") or (inp == "Y"):
        filename = input("Enter the File name: ")
        stAcc.fileInput(filename)
        stAcc.valueOf()
        
    else:
        stAcc.Create_new_Acc()