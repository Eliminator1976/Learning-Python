# time will be in format #:## or ##:##
time = input("What time is it? ")

def main():
    convert()
    
    
def convert():
    if time.find(':') == 1:
        w,x,y,z = list(time)
        w = float(w)
        y = float(y)
        z = float(z)
        time_num = 100*w + 10*y + z
        if time_num >= 700 and time_num <= 800:
            print("Time For BreakFast")
    elif time.find(':') == 2:
        w,x,y,z,e = list(time)
        w = float(w)
        x = float(x)
        z = float(z)
        e = float(e)
        time_num_1 = 1000*w + 100*x + 10*z + e
        if time_num_1 >= 1200 and time_num_1 <= 1300:
             print("Time For Lunch")
        elif time_num_1 >= 1800 and time_num_1 <= 1900:
            print("Time For Dinner")
    else:
        print("This is Not the Time to Have Meal!")
  
main()