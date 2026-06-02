menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
y = 0
y = float(y)
while True:        
    try:
        request = input("Item: ").title()
        if request in menu:
            y = y + float(menu[request])
            print(f"${y}")
        else:
            print(f"${y}")
            
        
    except EOFError:
        break
#this is the problem 2 of cs50p week3 problem set 3
    
        
