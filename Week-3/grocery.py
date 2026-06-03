grocery = {}

while True:
    try:
        item = input().upper().strip()
        if item in grocery:
            grocery[item] = grocery[item] + 1
        else:
            grocery[item] = 1
    except EOFError:
        for item in sorted(grocery): 
            print(f"{grocery[item]} {item}")
        break
        
