def main():
    while True:
        value = input("Fraction: ").split(sep="/")
        try:
            x = int(value[0])
            y = int(value[1])
            if x<0:
                continue
            if x/y*100 <= 1 :
                print("E")
            elif x/y*100>1 and x/y*100<99:
                percent = x/y*100
                print(f"{percent}%")
            elif x/y*100>= 99 and x/y*100<= 100:
                print("F")
            elif x/y*100>100:
                continue 
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break 

    
main()
