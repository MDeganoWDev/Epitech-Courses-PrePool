import re

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha2 = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
alphaR = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
alphaKey = "[abcdefghijklmnopqrstuvwxyz]"
result = ""
i = 0

print("Do you want to crypte or decrypte ?")
choice = input()

print("Choose a sentence :")
text = input()

print("Choose a key number :")
key = int(input())
if choice == "crypte" or choice == "decrypte" :
   while i < int(len(text)) :
   
       if int(len(re.findall(alphaKey, text[i]))) != 0 :
          x = 0
          check = False
   
          while check == False or x > int(len(alpha)):
              if text[i] == alpha[x]:
                  if choice == "crypte":
                     result += alpha[x-key]
                  else:
                     result += alpha[-(x-key)]

                  check = True
   
              else:
                  x += 1
       else :
           result += text[i]
       i += 1

print(result)