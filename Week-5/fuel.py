def main():
    remaining_fuel = input("Remaining Fuel in format x/y please: ")
    values = remaining_fuel.split("/")
    converted_value = convert(values)
    print(gauge(converted_value))


def convert(values):
    x = int(values[0])
    y = int(values[1])
    if x < 0 or x > y:
        raise ValueError("X cannot be negative")
    if y == 0:
        raise ZeroDivisionError
    return ((x/y)*100)


    


def gauge(percentage):
    if percentage <= 1:
        return f"E"
    if percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()