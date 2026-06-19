import sys
def main():
    try:
        match len(sys.argv):
            case _ if len(sys.argv) <2:
                sys.exit("Too few command-line arguments")
            case _ if len(sys.argv) >2:
                sys.exit("Too many command-line arguments")
                
                
        if sys.argv[1].endswith(".py"): 
            print(file_handler(sys.argv[1]))           
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File does'nt exist")

def file_handler(file_recieved):
    with open(file_recieved) as file:
        jerry = True
        i = 0       
        for line in file:
            # this is for the comment
            if line.startswith("#"):
                continue
            # this is for the blank line
            if len(line.lstrip()) == 0:
                continue
            #
            if "\"\"\"" in line:
                 if line.count("\"\"\"") == 2:
                     if not (line.lstrip().startswith("\"\"\"") or line.lstrip().startswith('#')):
                         pass
                     else:
                         i -= 1                        
                 else:
                     jerry = not jerry
                     if jerry == True:
                         i -= 1               
            if jerry == True:
                i += 1
            else:
                continue
          
        return i
        
main()
                
            

