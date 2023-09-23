# EXERCICE 0
mot = "Hello world !"
print("Exercice 0 :", mot.lower())

# EXERCIE 1
mot2 = "tutu on the tuki-kata"
print("Exercice 1 :", mot2.replace("tu", "ta"))

# EXERCICE 2
mot3 = mot.find("a")
print("Exercice 2 :", mot3)

# EXERCICE 3
mot4 = " abcdefghij "
print("Exercice 3 :",mot4[::-2][:5][::-1][3:])

# EXERCICE 4
print("Exercice 4 :",mot4[1::2][4:5])

# EXERCICE 5-6
print("Exercice 5-6 :",mot*10)

# EXERCICE 7
s1 = "hello"
s2 = 42
concat = s1+str(s2)
print(concat)

# EXERCICE 8
string1 = "42"
string2 = "is"
string3 = "the answer"
concat2 = "\""+string1+" "+string2+" "+string3+"\""
print("The string", concat2, "characters")
