lst = eval(input(" Enter a list: "))
max = lst[0]
for i in lst:
    if i>max:
        max = i

print("Highest Element is: ",max)

