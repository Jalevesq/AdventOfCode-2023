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
    "nine": 9,
    "eight": 8,
    "seven": 7,
    "six": 6,
    "five": 5,
    "fourth": 4,
    "three": 3,
    "two": 2,
    "one": 1,
    "zero": 0,
}



if __name__ == "__main__":
    input_path : str = 'input.txt'
    output : int = 0
    with open(input_path, 'r') as file:
        for line in file:
            print(line)
            # found_number =
            # output = output + found_number
    print(f"Total Number Output: {output}")

# 52974