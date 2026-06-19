import sys
import csv

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        elif (f"{sys.argv[1]}".endswith(".csv") and f"{sys.argv[2]}".endswith(".csv")):
            if file_handler(sys.argv[1],sys.argv[2]) == 1:
                print("Process Ended successfully")
        else:
            sys.exit("unsupported file extension")
    except FileNotFoundError:
        print("File Not in Directory")

def file_handler(input_file, output_file):
    name_list = []
    house_list = []
    with open(input_file,"r", newline="") as s:
        reader = csv.DictReader(s)
        for row in reader:
            name_list.append(row['name'].strip("'"))
            house_list.append(row['house'])
    first_name_list = []
    last_name_list = []
    for name in name_list:
        first_name,last_name = name.split(",")
        first_name_list.append(first_name)
        last_name_list.append(last_name.strip())
    with open(output_file, "a", newline='') as f:
        headers = ['first_name','last_name','house']
        writer = csv.DictWriter(f, fieldnames = headers)
        writer.writeheader()
        for first_name,last_name,house in zip(first_name_list,last_name_list,house_list):
            writer.writerow({"first_name":first_name,"last_name":last_name,"house":house})
    
main()
