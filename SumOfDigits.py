num = int(input("Enter a Number: "))
sum = 0

for i in range(0,num):
    sum = sum + num%10
    num = num//10

print("Sum of digits is: ",sum)