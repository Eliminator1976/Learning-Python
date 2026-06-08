import random


def main():
    level = get_level()

    while True:
        operator = input("Opearator: ")
        operators = ["-", "+", "*", "/"]
        if operator in operators:
            break
        else:
            continue
    j = 0
    k = 0
    while k < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        calc_data = [x, operator, y]

        i = 0
        real_answer = operator_handler(*calc_data)
        while i < 3:
            answer = int(input(f"{x} {operator} {y} = "))
            k += 1
            if answer == real_answer:
                j += 1
                break
            else:
                print("EEE")
                i += 1
                if i == 3:
                    print(f"{x} {operator} {y} = {real_answer}")
                else:
                    continue
    print("Great Game! \n" + "Your score is " + str(j * 10))


def operator_handler(x, operator, y):
    match operator:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            allowed_levels = [1, 2, 3]
            if n in allowed_levels:
                break
        except ValueError:
            continue

    return n


def generate_integer(level):
    start = 1 if level == 1 else 10 ** (level - 1)
    end = (10**level) - 1
    return random.randint(start, end)


if __name__ == "__main__":
    main()
