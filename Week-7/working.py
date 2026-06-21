import re
import os
import psutil

def main():
    print(convert(input("Hours: ")))

def convert(s):
    
    if matches := re.search(r"((?:[0-9]|[0-1][0-2])|(?:[0-9]:[0-5][0-9]|[0-1][0-2]:[0-5][0-9])) (AM|PM) to ((?:[0-9]|[0-1][0-2])|(?:[0-9]:[0-5][0-9]|[0-1][0-2]:[0-5][0-9])) (AM|PM)", s):
        cases = {"case_a": matches.group(1), "case_b": matches.group(3)}
        # note the time in given order
        hour_list = []
        min_list = []
        for case, time in cases.items():
            if ":" in time:
                hour_list.append(f"{int(time.split(':')[0]):02}")
                min_list.append(time.split(":")[1])
            else: # if time didnt had : then it will be an hour with 00 minutes else save the minutes in other list
                hour_list.append(f"{int(time):02}")
                min_list.append("00")
        # split the time str and take the hour number        
        cases_1 = {"case_a": matches.group(2),"case_b": matches.group(4)}
        i = 0
        for case,median in cases_1.items(): 
            if median == "PM":
                if hour_list[i] == "12":
                    i += 1
                    continue
                else:
                    hour_list[i] = int(hour_list[i]) + 12
                    i += 1
            if median == "AM":
                if hour_list[i] == "12":
                    hour_list[i] = "00"
                i += 1            
        # if time was in pm, add 12 to hour number              
        # till here we get hour in 24hr , mins in other list 
        final_list = []
        for hour, mins in zip(hour_list,min_list):
            final_list.append(f"{hour}:{mins}")

        return f"{final_list[0]} to {final_list[1]}"
    else:
        raise ValueError("time format error/e404")
   

if __name__ == "__main__":
    main()
process = psutil.Process(os.getpid())
print(f"Current process memory: {process.memory_info().rss/(1024**2)} megabytes")
  