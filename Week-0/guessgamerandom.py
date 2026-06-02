from random import randint
secret = randint(1, 10)
print("Welcome to the Guessing Game")
guess = 0
while guess != secret:
    g = input("Type a number ")
    guess = int(g)
    if guess == secret:
        print("congrats, u win")
    if guess > secret:
        print("too high")
    if guess < secret:
        print("too low")
            
    

       
    