def switch():
    value=int(input("Enter the value for temperatur Conversion "))
    option=int(input("choose option 1-> fahrenheit 2->celsius "))
    def fahrenheitt():
        result=(value*(9/5))+32
        print(result)
    def celsius():
        result=(value-32)*(5/9)
        print(result)
    dictionary={1:fahrenheitt,
                2:celsius }
    dictionary.get(option)()

 
switch()