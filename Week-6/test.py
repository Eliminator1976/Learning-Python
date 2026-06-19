import csv
import sys

def main():
    print(file_handler(sys.argv[1],sys.argv[2]))

def file_handler(input_file, output_file):
    with open(input_file,"r", newline="") as s:
        reader = csv.DictReader(s)
        meow = []
        for line in reader:
            meow.append(line)
            print(meow)
main()