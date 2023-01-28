print("Hello World!")

print ("Press 1 for reverse\n Press 2 for sum of the product")

ch = int(input())
print ("Enter the first input -")
a = int(input())
print ("Enter the second input -")
b = int(input())

match ch:
    case 1: num = 1542
      sum = 0
      while num != 0
      dig = num % 10
      sum = sum*10+ dig
      num = math.floor(num/10)
      print (sum)
    case _: print("Wrong choice")
