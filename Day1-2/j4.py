number1 = 12.24
number2 = 424242.8412

int1 = int(number1)
int2 = int(number2)

str1 = str(number1)
str2 = str(number2)

final1 = str1[len(str(int1))+1:]
final2 = str2[len(str(int2))+1:]

print("l'entier du chiffre 1 est :",int1)
print("l'entier du chiffre 2 est :",int2)
print("la decimal du chiffre 1 est :",final1)
print("la decimal du chiffre 2 est :",final2)