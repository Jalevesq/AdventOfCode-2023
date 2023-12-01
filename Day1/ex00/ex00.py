import re

#########
# [--- Part One ---]
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value
# that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
# to form a single two-digit number.
# For example:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# Consider your entire calibration document. What is the sum of all of the calibration values?
#########

class FoundNumber:
    def __init__(self, number, index):
        self.number = number
        self.index = index


def find_first_number(line: str) -> str:
    match = re.search(r'\d', line)
    if match:
        return FoundNumber(match.group(0), match.start(0))
    return FoundNumber("", "")

def find_last_number(line: str) -> str:
    match = re.search(r'\d(?=[^\d]*$)', line)
    if match:
        return FoundNumber(match.group(0), match.start(0))
    return FoundNumber("", "")

def get_number(line: str) -> int:
    first = find_first_number(line)
    last = find_last_number(line)

    number = ""
    if first.index != -1:
        number = number + first.number
    if last.index != -1:
        number = number + last.number
    return number

if __name__ == "__main__":
    input_path : str = '../input.txt'
    output : int = 0
    with open(input_path, 'r') as file:
        for line in file:
            found_number = int(get_number(line))
            output = output + found_number
    print(f"Total Number Output: {output}")

# 52974