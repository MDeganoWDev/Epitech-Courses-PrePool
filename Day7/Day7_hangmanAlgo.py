from colorama import Fore
from Day7_hangmanDrawning import hangmanDrawning, hangmanCharacter
from Day7_hangmanList import wordGen

def hangman (hp) :
    maxHp = hp
    hangmanCharacter(hp)
    word = wordGen()
    answer = "_"*len(word)
    alreadyFound = []

    while hp > 0 :
        charSelected = ""
        found = False
        alreadyExist = False

        while len(charSelected) != 1 or alreadyExist == True : 
            if len(alreadyFound) > 0 :           
                print(Fore.BLUE, alreadyFound)

            charSelected = input(Fore.RESET+"Select a character : ").lower()

            if charSelected.upper() in alreadyFound : 
                alreadyExist = True
                print(Fore.BLUE+"You already selected the letter :", charSelected.upper())
            else :
                alreadyExist = False
                alreadyFound.append(charSelected.upper())

        for i in range(len(word)) :            
            if  word[i] == charSelected and answer[i] != charSelected :
                answer = answer[:i] + charSelected + answer[i+1:]
                found = True

        if answer == word :
            print(Fore.GREEN +"/!\ YOU WIN /!\ \nYou found the word :", word)
            break

        elif found == True :
            print(Fore.GREEN +"Congratulation \""+charSelected.upper()+"\" exist\nYour word is :", answer)
        
        else :
            hp -= 1            
            if hp == 0 :
                hangmanDrawning(hp,maxHp)
                print(Fore.RED +"/!\ YOU LOOSE /!\ \nThe word was :", word) 
            
            else :
                hangmanDrawning(hp, maxHp)
                print(Fore.RED +"Sorry \""+charSelected.upper()+"\" dosn't exist, you have", hp, "hp left\nYour word is :", answer)
    