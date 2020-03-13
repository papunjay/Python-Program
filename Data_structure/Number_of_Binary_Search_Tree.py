def Number_of_BST(Number):
    no_of_Node=Factorial(2*Number)//(Factorial(Number+1)*Factorial(Number))
    return no_of_Node
    
Test_case=int(input("Number of test case... "))
while Test_case >0:
    Number=int(input("Enter the Number of node... "))
    result=Number_of_BST(Number)
    print(result)
    Test_case-=1