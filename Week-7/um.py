import re
import sys


def main():
    print(count(input("Text: ")))
# return 0 if no "um" and 1 for each "um

def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return int(int(len(matches)))

if __name__ == "__main__":
    main()
# didnt make um_test.py cuz this is pretty simple project and idk if it needs that much of attention