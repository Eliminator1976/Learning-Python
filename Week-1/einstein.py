x = int(input("Welcome, Please provide a mass value in (kg) "))
print("by default, value of 'c',speed of light is 3*10^8")

def formula(x):
    
    e = int((x *(3 * 10**8)**2)/10**16)
    return e
def main() :
    e=formula(x)
    print("The energy produced is ", e ,"*10^16", "joules")
    
    
    
main()
    