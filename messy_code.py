def add_numbers(a: float, b: float) -> float:
    return a + b


def get_number(prompt: str) -> float:
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main() -> None:
    print("=== Simple Adder Program ===")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()
