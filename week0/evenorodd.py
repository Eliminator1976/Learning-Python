def main():
    x = int(input("whats x "))
    if is_even(x) == True:
        print("x is even")
    else:
        print("x is odd")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
main()
    