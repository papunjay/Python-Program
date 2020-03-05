import random
Stake=int(input("Enter The Stak value="))
Goal=int(input("Enter your Goal="))
Number=int(input("Enter The Number of itration you want to play="))
win=0
loose=0
for i in range(Number):
    ran_Number=(random.randint(1,Stake))
    #print(ran_Number)
    if(ran_Number>Goal):
        win+=1
    else:
        loose+=1
win_per=(win*100)/Number
loose_per=(loose*100)/Number
print("No of Win={}".format(win))
print("percentage of win = {} %".format(win_per))
print("percentage of loose = {} %".format(loose_per))