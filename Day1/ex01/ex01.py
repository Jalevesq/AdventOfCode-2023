import re

#########
# [--- Part Two ---]
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
#
# What is the sum of all of the calibration values?
#########

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "fourth": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_number(line: str) -> int:
    first = 0
    last = 0
    for c in line:
        if c.isdigit():
            if first == 0:
                first = int(c)
            else:
                last = int(c)
    if last == 0:
        return [first * 10, first]
    return [first * 10, last]

def get_total(content: str) -> int:
    number = 0
    for line in content:
        number = number + sum(get_number(line))
        # break
    return number


if __name__ == "__main__":
    input_path : str = '../input.txt'
    output : int = 0
    with open(input_path, 'r') as file:
        content = file.read()
    content = content.split('\n')
    total_number = get_total(content)
    print(total_number)