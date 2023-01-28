import math
print ("Enter 1 for finding the reversal of number")

ch = int(input())

match ch:
    case 1: 
        print("enter a number")
        num = int(input())
        sum = 0 
        while num!=0:
            dig = num % 10
            sum = sum * 10 + dig
            num = math.floor(num/10)
        print(sum)
    case _:
        print("Wrong choice")
