def make_smoothie():
    juice = input("What juice would u like? ")
    fruit = input("OK - and how about the fruit? ")
    print("Crushing the ice...")
    print("Blending the " + fruit)
    print("Now adding in the " + juice + " juice")
    print("Finished! There's your " + fruit + " and " + juice + " smoothie!")

print("Welcome to smoothie-matic 2.0")
another = "Y"
while another == "Y":
    make_smoothie()
    another = input("How about another(Y/N)? ")