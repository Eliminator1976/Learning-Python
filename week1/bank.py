greet = input("Greeting: ").title().strip()


def greeting_with_h(greet):
    ques = greet.find("H")
    
    if ques == 0 and greet.find("Hello") == 0:
            print('0')
            
    elif ques == 0:
        print('20')
        
    else:
        print('100')

greeting_with_h(greet)
            