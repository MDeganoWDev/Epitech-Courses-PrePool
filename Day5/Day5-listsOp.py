############################ EXERCICE 01 ###############################
#
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list:
    list[i] = list[i]*i
print("Exercice 1 : ", list)

############################ EXERCICE 02 ###############################
#
list = [x + 10 for x in [3, 2, 6, 7, 1, 4]]
# ADD +10 TO ALL NUMBER IN THE ARRAY
print("Exercice 2 : ", list)

############################ EXERCICE 03 ###############################
#
# list(map(lambda x: x*x, [3, 2, 6, 7, 1, 4]))
# print("Exercice 3 : ", list)
#
# ????????????????????
# 

############################ EXERCICE 04 ###############################
#
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Exercice 4 : ", min(list), max(list))

############################ EXERCICE 05 ###############################
#
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
for i in list:
    if list[i] < 7:
        list2.append(list[i])
print("Exercice 5 : ", list2)

############################ EXERCICE 06 ###############################
#
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Exercice 6 : ", sorted(list, reverse=True))

############################ EXERCICE 07 ###############################
#
list = [x//2 if x%2 == 0 else x *2 for x in [42, 3, 4, 18, 3, 10]]
# SI LE CHIFFRE EST PAIRE ON LE DIVISE PAR 2 SINON ON MULTIPLIE PAR 2
print("Exercice 7 : ", list)

############################ EXERCICE 08 ###############################
#
# list = list(filter(lambda x : x>10, [42, 3, 4, 18, 3, 10]))
# print("Exercice 8 : ", list)
#
# ????????????????????
# 

############################ EXERCICE 09 ###############################
#
list = [*enumerate([42, 3, 4, 18, 3, 10])]
print("Exercice 9: ", list)

############################ EXERCICE 10 ###############################
#
first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
magic = [*zip(first_name, last_name[::-1])]

print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])