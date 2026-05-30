def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
nope = ' .,!&-_'
nope = list(nope)
number = '0123456789'
number = list(number)

def is_valid(s):
    p = list(s)
    if len(p) <2 or len(p)>6:
        return False
    for i in s[0:2]:
        if i.isalpha() == False:
            return False
    for i in nope:
        if i in p:
            return False
    for num in p:
        if num.isdigit():
            if num == '0':
                return False
            break
    for i in number:
        if i in p:
            n = p.index(i)
            break
    for i in s[n:]:
        if i.isdigit() == False:
            return False
    else:
        return True

main()

#start with atleast two letters
#maximum of 6characters letters or numbers and minimum 2
#numbers should not be between letters
# and first number not 0
#no periods spaces punctuation marks allowed