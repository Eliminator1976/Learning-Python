def convert(x):
    
    x=x.replace(':)', '\U0001F600')
    x=x.replace(':(', '\U0001F641')
    return x

def main():
     y=input("Share some text with emojis ")
     print(convert(y))
     
main()    

    
    