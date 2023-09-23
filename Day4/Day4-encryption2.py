import re

alphaArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphaArrayR = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
alphaKey = "[abcdefghijklmnopqrstuvwxyz]"
alpha = []
result = ""
i = 0
x = 0

print("Do you want to crypte or decrypte ?")
choice = input()

print("Choose a sentence :")
text = input()

print("Choose a key number :")
key = input()

if choice == "crypte" or choice == "decrypte" :
   
   while len(alpha) != len(text):
       
       if int(len(re.findall(alphaKey, text[i]))) != 0 :
           if len(key)-1 > x :
               alpha.append(ord(key[x])-97)
               x += 1
           elif len(key)-1 == x:
               alpha.append(ord(key[x])-97)
               x=0

   while i < int(len(text)) :
   
       if int(len(re.findall(alphaKey, text[i]))) != 0 :
          y = 0
          check = False
   
          while check == False or y > int(len(alphaArrayR)):
              if text[i] == alphaArrayR[y]:
                  if choice == "crypte":                      
                    result += alphaArrayR[y-alpha[i]]
                  else:
                     print(alphaArrayR[-y - -alpha[i]], -y, -alpha[i], -y - -alpha[i])
                     result += alphaArrayR[-y - -alpha[i]]
                  check = True 
              else:
                  y += 1
       else :
           result += text[i]
       i += 1

print(result)