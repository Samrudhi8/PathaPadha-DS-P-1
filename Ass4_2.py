lst = eval(input("Enter a list: "))
min = lst[0]

for i in range(1,len(lst)+1):
    for j in range(i+1,len(lst)):
        if (lst[i] > lst[j]):
            min = lst[i]
            lst[i] = lst[j]
            lst[j] = min


print(lst)