names = []
name_list= []
x = "Adieu, adieu, to "
def main():
    while True:
        try:
            names.append(input("Name: ").strip().title())
        except EOFError:
            print()
            print()
            if len(names) == 1:
                print(x+names[0])
                break
            if len(names) == 2:
                print(x+names[0]+" and "+names[1])
                break
            elif len(names)>2:
                for name in names[0:-1]:
                    name_list.append(name)
                print(x + ', '.join(name_list) + ", and "+ names[-1])
                break
        
                    
main()
                
                
    
