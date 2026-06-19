import csv
import tabulate
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        elif sys.argv[1].endswith(".csv"):
            print(file_handler(sys.argv[1]))
        
        else:
            print("unsupported file extension")
    except FileNotFoundError:
        print("File Not in Directory")

def file_handler(file):
    with open(file) as f:
        type_pizza = file.title().split(".")[0]
        content = csv.reader(f)
        headers = [f"{type_pizza} Pizza","Small","Large"]
        next(content)
        table = []
        for lines in content:
            table.append(lines)
        return tabulate.tabulate(table,headers,tablefmt="grid")

main()