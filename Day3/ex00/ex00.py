
def getCoord(splitContent: list):
    number_coords = []
    symbol_coords = []

    for y, line in enumerate(splitContent):
        x = 0
        while x < len(line):
            char = line[x]

            if char.isdigit():
                start_x = x
                while x < len(line) and line[x].isdigit():
                    x += 1
                end_x = x - 1
                number_coords.append({"number": line[start_x:end_x + 1], "coords": (start_x, y, end_x, y)})

            elif not (char.isdigit() or char == '.'):
                symbol_coords.append({"symbol": line[x + 1], "coords": (x, y)})

            x += 1

    return number_coords, symbol_coords
    
    return number, symbol

def main(splitContent):
    numbers, symbols = getCoord(splitContent)
    for number in symbols:
        print(number)
    
    
with open('../input.txt', 'r') as f:
    content = f.read()

splitContent: list = content.split('\n')
main(splitContent)


# def checkIfNumber(idx: int, idx2: int, splitContent: list) -> int:
#     number = 0
#     length = len(splitContent)
#     lineLength = len(splitContent[idx])
#     if idx2 
#     if idx - 1 >= 0:
#         ;
#     if idx + 1 < length:
#         ;



# def main(splitContent):
#     total_sum: int = 0
#     for idx, line in enumerate(splitContent):
#         for idx2, char in enumerate(line):
#             if not char.isdigit() and char is not '.':
#                 total_sum = total_sum + checkIfNumber(idx, idx2, splitContent)
#         if idx == 3:
#             break

# with open('../input.txt', 'r') as f:
#     content = f.read()

# splitContent: list = content.split('\n')
# main(splitContent)