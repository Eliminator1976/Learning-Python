from random import randint
from numb3rs import validate
import time
# this solution is not for cs50p, i just wanted to try time lib and abit beautification
def test_numb3rs():
    print(f"processing... this might take a while!")
    for i in range(10):
        time.sleep(0.2)
        ip = parser(*numgen())
        if validate(ip) == True:
            print(f"ip: {ip}, True")
        else:
            print(f"ip: {ip}, False")

def parser(a,b,c,d):
    return f"{a}.{b}.{c}.{d}"
def numgen():
    list_o_int = []
    for i in range(4):
        list_o_int.append(randint(0,255))
    return list_o_int
test_numb3rs()