############################ EXERCICE 00 ###############################

# word = input("Select a word : ")
# number = int(input("Select a number : "))

# def A (word, number) :
#     found = [letter for letter in word if letter.islower()]
#     if len(found) >= number :
#        return True
#     else : 
#        return False
    
# def B (word, number) :
#     found = [letter for letter in word if letter.isupper()]
#     if len(found) >= number :
#        return True
#     else : 
#        return False

# def C (word, number) :
#     found = [letter for letter in word if letter.isalpha()]
#     if len(found) >= number :
#        return True
#     else : 
#        return False

# def D (word, number) :
#     found = [letter for letter in word if not letter.isalnum()]
#     if len(found) >= number :
#        return True
#     else : 
#        return False

# def E (word, number) :
#     found = [letter for letter in word if letter.isnumeric()]
#     if len(found) >= number :
#        return True
#     else : 
#        return False

# print(A(word, number))
# print(B(word, number))
# print(C(word, number))
# print(D(word, number))
# print(E(word, number))

############################ EXERCICE 01 ###############################

def check_password (type, number, password) :
    if type == "lower" : found = [letter for letter in password if letter.islower()]
    if type == "special" : found = [letter for letter in password if not letter.isalnum()]
    if len(found) >= number :
       return True
    else : 
       return False

mysecretpassword = input("Select a new password : ")
if check_password ("lower", 4, mysecretpassword) == True and check_password ("special", 2, mysecretpassword) == True :
   print("Password registered !")
else :
   print("Password not secured enough !")

############################ EXERCICE 02 ###############################

check = False
def check_password (type, number, password) :
    if type == "lower" : found = [letter for letter in password if letter.islower()]
    if type == "special" : found = [letter for letter in password if not letter.isalnum()]
    if len(found) >= number :
       return True
    else : 
       return False
    
while check == False :
    mysecretpassword = input("Select a new password : ")
    if check_password ("lower", 4, mysecretpassword) == True and check_password ("special", 2, mysecretpassword) == True :
       print("Password registered !")
       check = True
    else :
       print("Password not secured enough !")
