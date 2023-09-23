i = 0

number1 = str(345567426)
number2 = str(44490320097)

somme1 = 0
somme2 = 0

len1 = len(number1)
len2 = len(number2)

while len1 > i:
   somme1 = somme1 + int(number1[i])
   i = i+1

i = 0

while len2 > i:
   somme2 = somme2 + int(number2[i])
   i = i+1

print(somme1, somme2)