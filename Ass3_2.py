string = input("Enter a String: ")
if(len(string) < 3):
    print(string)
else:
    if(string.find("ing") == -1):
        print(string+"ing")
    else:
        print(string+"ly")