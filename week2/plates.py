def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(s):
    p = list(s)
    if len(list(p)) <2 or len(list(p)) >6:
        return False
    for i in s[0:2]:
        if i.isalpha == True:
            return True
    elif numinchar(s) == False:
        return True
    elif nspclchr(s) == True:
        return True
    
def numinchar(s):
    s = list(s)
    nums = '0123456789'
    p = list(nums)
    
            
            
def nspclchr(s):
    p = list(s)
    spcl = ['!','@','#','$','%','&','*']
    for i in p:
        if set(i).isdisjoint(spcl)
        return True
    else:
        return False
    
# checks for no special characters
    
    

main()

#start with atleast two letters
#maximum of 6characters letters or numbers and minimum 2
#numbers should not be between letters and first number not 0
#no periods spaces punctuation marks allowed