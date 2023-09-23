import random

myFile = open("Day7_hangmanList.txt", "r")
wordList = myFile.read().splitlines()

def wordGen () :
    return random.choice(wordList).lower()