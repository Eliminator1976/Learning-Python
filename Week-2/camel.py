reply = input("camelCase: ")
print("snake_case: ", end="")
for char in reply:
    if char == char.lower():
        print(char, end="")
    else:
        print("_" + char.lower(), end="")
print()  
