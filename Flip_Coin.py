import random
Head_count=0
Tail_count=0
print("Enter The number of times to Flip Coin")
Number=int(input())
for x in range(0,Number):
    random_value=(random.random())
    if random_value > 0.5 :
        print("HEAD")
        Head_count=Head_count+1
    else:
        print("TAILS")
        Tail_count=Tail_count+1
head_percentage=((Head_count*100)/Number)
Tail_percentage=((Tail_count*100)/Number)
print("head_percentage is = {}".format(head_percentage))
print("Tail_percentage is = {}".format(Tail_percentage))

