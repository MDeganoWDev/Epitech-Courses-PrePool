from Day7_hangmanAlgo import hangman

while 1==1 :
    try :
        hp = int(input("Select a number of life beetween 5 and 15 : "))
    except :
        print("error")
    else :
        if hp >= 5 and hp <= 15 :
            hangman(hp)
            break
            