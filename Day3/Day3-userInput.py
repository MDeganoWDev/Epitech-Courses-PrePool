# EXERCIE 0
# print("EXERCICE 0 :")
# print("What's your name ?")
# name = input()
# print("Hello", name)

# EXERCIE 1
# print("EXERCICE 1 :")
# print("What's your name ?")
# name = input()
# nameTrs = name.capitalize()
# print("Hello", nameTrs)


# EXERCIE 2
# print("EXERCICE 2 :")
# print("Choose a first number")
# n1= input()
# print("Choose a second number")
# n2= input()
# somme = int(n1)+int(n2)
# print("the sum of "+n1+" + "+n2+" is :"+str(somme))

# EXERCIE 3
# print("EXERCICE 3 :")
# print("choose a whole number :")
# num= int(input())
# print(type(num))

# EXERCIE 4
print("EXERCICE 4 :")
phrase= "This is a test. Is it possible to fly ? Good things come to those who never give up."
phraseClean=phrase.replace("?",".").replace("!",".")
mot3=phraseClean.split(". ")
result=""
i=0

for mot in mot3:
    mot4 = mot.split(" ")
    if i== mot3[-1]:
          result += mot4[i]+"."
    else:
          result += mot4[i]+" "
print(result)