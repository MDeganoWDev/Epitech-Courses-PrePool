############################ EXERCICE 01 ###############################
#
list = [1, 2, 3, 4, 5]
print("Exercice 1 : ", list[0])

############################ EXERCICE 02 ###############################
#
list = [1, 2, 3, 4, 5]
print("Exercice 2 : ",list[-1])

############################ EXERCICE 03 ###############################
#
list = [1, 2, 3, 4, 5]
list.append(6)
print("Exercice 3 : ",list[-1])

############################ EXERCICE 04 ###############################
#
list = [1, 2, 3, 4, 5]
print("Exercice 4 : ",list)

############################ EXERCICE 05 ###############################
#
list = [1, 2, 3, 4, 5]
list.pop(-1)
print("Exercice 5 : ",list)

############################ EXERCICE 06 ###############################
#
list = [1, 2, 3, 4, 5]
list.insert(0 ,0 )
print("Exercice 6 : ",list)

############################ EXERCICE 07 ###############################
#
list = [1, 2, 3, 4, 5]
print("Exercice 7 : ",list[1:4])

############################ EXERCICE 08 ###############################
#
list = [1, 2, 3, 4, 5]
print("Exercice 8 : ",list[::-1])

############################ EXERCICE 09 ###############################
#
list = [1, 2, 3, 4, 5]
print("Exercice 9 : ",list[::2])

############################ EXERCICE 10 ###############################
#
list = [1, 2, 3, 4, 5]
i = 6
while i <= 17 :
    list.append(i)
    i += 1
print("Exercice 10 : ",list)
############################ EXERCICE 11 ###############################
#
my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list.extend( my_second_list )
print(my_first_list)

my_first_list = [7 , 8 , 9]
my_second_list = [4 , 5 , 6]
my_first_list = [* my_first_list , * my_second_list ]
print(my_first_list)
