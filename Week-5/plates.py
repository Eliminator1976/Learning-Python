def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = list(s)
    if len(s) <2 or len(s) > 6:
        return False
    for char in s[0:2]:
        if not char.isalpha():
            return False
    numbers = list("0123456789")
    list_nums = []
    for char in s:
        if char in numbers:
            list_nums.append(char)
            break
    if list_nums[0] == "0":
        return False
    else:
        x = list_nums[0]
        y = s.index(x)        
    for num in s[y:]:
        if not num.isdigit():
            return False
    spclchars = list("! ?.,")
    for schar in spclchars:
        if schar in s:
            return false
    else:
        return True


if __name__ == "__main__":
    main()