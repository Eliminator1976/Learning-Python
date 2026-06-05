months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        date = input("Date: ").title()
        if "/" in list(date):
            # format = MM/DD/YYYY
            date_analog = date_analog_handler(date)
            print(date_analog)
            break
        elif "," in list(date):
            # format = month day, year
            date_easy = date_easy_handler(date)
            print(date_easy)
            break
        else:
            print("unsupported format error")
            break


def date_analog_handler(date):
    date = date.split(sep="/")
    # becomes a list as ['MM','DD','YYYY']

    if int(date[0]) > 12 or int(date[1]) > 31:
        return f"unpossible date 😭"

    if not date[0].startswith("0") and not date[0].startswith("1"):
        date[0] = date[0].replace(date[0], "0" + date[0])
    if (
        not date[1].startswith("0")
        and not date[1].startswith("1")
        and not date[1].startswith("2")
        and not date[1].startswith("3")
    ):
        date[1] = date[1].replace(date[1], "0" + date[1])
    return f"{date[2]}-{date[0]}-{date[1]}"


# temp paste (# format = month day, year)


def date_easy_handler(date):
    date = date.replace(",", "").split()
    # becomes a list as ['month', 'day', 'year']
    try:
        x = months.index(date[0]) + 1
        if x < 10:
            date[0] = f"0{str(x)}"
        else:
            date[0] = str(x)

    except ValueError:
        return f"unknown month"

    # month became a number without 0 formatting
    if int(date[1]) > 31:
        return f"unpossible date 😭"

    if not date[0].startswith("0") and not date[0].startswith("1"):
        date[0] = date[0].replace(date[0], "0" + date[0])
    if (
        not date[1].startswith("0")
        and not date[1].startswith("1")
        and not date[1].startswith("2")
        and not date[1].startswith("3")
    ):
        date[1] = date[1].replace(date[1], "0" + date[1])
    # month and date get 0 formatted
    return f"{date[2]}-{date[0]}-{date[1]}"


main()
# YYYY-MM-DD required format
