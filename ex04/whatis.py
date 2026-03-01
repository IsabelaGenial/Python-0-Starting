import sys


def is_even_or_odd(number) -> str:

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():

    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: Please provide a valid integer.")
        return

    result = is_even_or_odd(number)
    print(f"I'm {result}.")


if __name__ == "__main__":
    main()
