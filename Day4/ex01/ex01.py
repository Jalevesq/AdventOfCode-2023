def getCardID(line: str) -> str:
    cardID = ""
    for c in reversed(line):
        if not c.isdigit():
            break
        cardID = c + cardID
    return cardID


def addCard(listCard, cardID, totalWin, numberOfCard):
    i = 0
    while i < numberOfCard:
        j = 1
        while j <= totalWin:
            currentWin = listCard[cardID + j]
            listCard[cardID + j] = currentWin + 1
            j = j + 1
        i = i + 1

    return listCard

# idx: 0 = cardID, 1 = winningNumber, 2 = numberIHave
def getNumberWinningCard(currentCard, listCard):
    numberOfCard = listCard[currentCard[0]]
    totalWin = 0
    for number in currentCard[2]:
        if number in currentCard[1]:
            totalWin = totalWin + 1
    listCard = addCard(listCard, currentCard[0], totalWin, numberOfCard)

    return listCard

def getSumCard(line: str, listCard : dict) -> int:
    idx1: int = line.find(":")
    idx2: int = line.find('|')

    winningNumber: list = line[idx1 + 1: idx2].split()
    numberIHave: list = line[idx2 + 1:].split()
    cardID = int(getCardID(line[:idx1]))

    numberToPlay = listCard[cardID]
    listCard[cardID] = numberToPlay + 1

    currentCard = [cardID, winningNumber, numberIHave]

    listCard = getNumberWinningCard(currentCard, listCard)

    return listCard


def initList(lenToInit):
    listCard: dict = {}
    i = 0
    while i <= lenToInit:
        listCard[i] = 0
        i = i + 1
    return listCard

if __name__ == "__main__":
    with open('../input.txt', 'r') as f:
        content = f.read()
    splitContent = content.split("\n")

    listCard: dict= initList(len(splitContent)) 
    for line in splitContent:
        listCard = getSumCard(line,listCard)
    
    totalSum = 0
    i = 1
    while i <= len(splitContent):
        totalSum = totalSum + listCard[i]
        i = i + 1
    print(totalSum)

# 13768818