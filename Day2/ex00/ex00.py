import re

# --- Part One ---
# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag,
# grab a handful of random cubes, show them to you, and then put them back in the bag.
# He'll do this a few times per game.
#
# You play several games and record the information from each game (your puzzle input).
# Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list
# of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again).
# The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration.
# However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; 
# similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once.
# If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
# What is the sum of the IDs of those games?
# 2237



class BagOfCube:
    def __init__(self):
        self.red: int = 12
        self.green: int = 13
        self.blue: int = 14
    
    def getColor(self, color):
        return getattr(self, color, None)
    
    def getPossibility(self, splitScores):
        color = splitScores[1]
        number = int(splitScores[0])
        numberOfCubes = self.getColor(color)
        if numberOfCubes is not None and number <= numberOfCubes:
            return True
        return False
        

def getGameID(line: str) -> int:
    match = re.search(r"\d+", line)
    gameID = int(match.group())
    return gameID


def isRoundPossible(roundScores):
    bag = BagOfCube()
    for scores in roundScores:
        splitScores = scores.split(' ')
        isPossible = bag.getPossibility(splitScores)
        if isPossible is False:
            return False
    return True
        


def IsGamePossible(line):
    splitLine = line.split(':')
    allRoundPlayed = splitLine[1].split(';')
    for round in allRoundPlayed:
        roundScores = [score.strip() for score in round.split(',')]
        if isRoundPossible(roundScores) is False:
            return False

    return True


def getSum(split_content: list) -> int:
    gameIDSum: int = 0
    for line in split_content:
        isPossible = IsGamePossible(line)
        if isPossible is True:
            gameIDSum = gameIDSum + getGameID(line)
    return gameIDSum


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        content = f.read()
    split_content = content.split('\n')
    sum_of_game_played = getSum(split_content)
    print(sum_of_game_played)
    
    