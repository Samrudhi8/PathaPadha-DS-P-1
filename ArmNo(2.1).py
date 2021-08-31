num = int(input("Enter a Number: "))
sum = 0
var = num
while var > 0:
    r = var%10
    sum += r*r*r
    var //= 10

if num == sum:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
