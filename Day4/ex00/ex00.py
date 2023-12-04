def getWinningSum(line: str) -> int:
    idx1: int = line.find(":")
    idx2: int = line.find('|')
    winningNumber: list = line[idx1 + 1: idx2].split()
    numberIHave: list = line[idx2 + 1:].split()

    totalWin = 0
    for number in numberIHave:
        if number in winningNumber:
            if totalWin == 0:
                totalWin =  1
            else:
                totalWin = totalWin * 2
    return totalWin


if __name__ == "__main__":
    with open('../input.txt', 'r') as f:
        content = f.read()
    splitContent = content.split("\n")
    total = 0
    for line in splitContent:
        total = total + getWinningSum(line)
    print(total)