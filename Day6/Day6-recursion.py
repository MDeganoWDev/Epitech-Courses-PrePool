############################ EXERCICE 01 ###############################

word1 = "kayak"
word2 = "never odd or even"
word3 = "Was it a car or a cat I saw?"

def palyndrome(word, count, newWord="") :
    if count == 0 : 
        newWord = word.lower().replace("?", "").replace(" ", "")
    if count < len(word)/2 and newWord[count] == newWord[-(count+1)]:
        palyndrome(word, count + 1, newWord)
    elif newWord[count] != newWord[-(count+1)]:
        print(word, " n'est pas un palyndrome")
    else :
        print(word, " est un palyndrome")

palyndrome(word1, 0)
palyndrome(word2, 0)
palyndrome(word3, 0)

############################ EXERCICE 02 ###############################

import os
path = "/mnt/c/Users/DMatt/Documents/Pre-pool/"

def read (path) :
    dirList = os.listdir(path)
    print(path, ":", "\n", dirList)
    for dir in dirList :
        thisDir = os.path.join(path, dir)
        if os.path.isdir(thisDir) :
          read(thisDir)

read(path)