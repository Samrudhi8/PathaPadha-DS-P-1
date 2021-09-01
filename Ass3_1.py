string = input("Enter a String: ")

if len(string) > 2:
    print(string[0] + string[1] + string[len(string)-2] + string[len(string)-1])
else:
    print("Empty String")