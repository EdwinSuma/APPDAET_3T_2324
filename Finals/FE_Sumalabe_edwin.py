from pathlib import Path

input_path = Path("input.txt")
input_path.write_text("111\n156\n157\n192\n193\n195\n198\n204\n208\n210\n")

def get_sum(digits: list[int]) -> int:
    # 03: function that will calculate the sum of all integers in a list
    return sum(digits)
    pass

def get_digits(number: int) -> list[int]:
    #02: function to "breakdown" an integer into a list of integers
    return [int(digit) for digit in str(number)]
    pass

def is_harshad(number: int) -> bool:
    #01: function that determines if a given integer is a Harshad number
    digits = get_digits(number)
    return number % get_sum(digits) == 0
    pass

def main() :
    input_path = Path("input.txt")
    number_list = [int(number.strip()) for number in input_path.read_text().splitlines()]


    output_lines = [f"{number} - {is_harshad(number)}" for number in number_list]
    #04: write the results in a file named output.txt
    #use the following format:
    #
    # 111 - true
    # 112 - true
    # 113 - false

    output_path = Path("output.txt")
    output_path.write_text("\n".join(output_lines))

if __name__ == "__main__":
    main()