def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    p = list(s)
    if 6 < len(list(p)) < 2:
        return False
    for i in s[0:2]:
        if i.isalpha == True:
            return True
    elif i in s[0:1] == 0:
        return False
    elif numinchar(s) == False:
        return True
    
def numinchar(s):
    p = list(s)
    

main()

#start with atleast two letters
#maximum of 6characters letters or numbers and minimum 2
#numbers should not be between letters and first number not 0
#no periods spaces punctuation marks allowed