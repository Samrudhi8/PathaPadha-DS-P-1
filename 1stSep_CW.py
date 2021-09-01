string1 = input("Enter a string: ")
string2=""
for i in range(0,len(string1)):
    if string1[i].isupper():
        string2 += string1[i].lower()
    elif string1[i].islower():
        string2 += string1[i].upper()
    else:
        string2 += string1[i]
print(string2)
