from colorama import Fore

def hangmanDrawning (hp, maxHp) :
  maxHp = maxHp + 1
  for line in pendu[:maxHp-hp] :
    print(Fore.RED+line)
  for line in pendu[(maxHp+1)-hp:] :
    print(Fore.RED+line[0:5])

def hangmanCharacter(maxHp) :
  if maxHp > 5 :
    for i in range(int(maxHp-5)) :
      pendu.insert(2, linePlus)

linePlus = " |       |"
pendu = [
"______________",
" |/      |",
" |      (_)",
" |      /|\ ",
" |       |",
" |      / \ ",
" |",
"_|___",
]