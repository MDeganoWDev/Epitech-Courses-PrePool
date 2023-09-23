############################ EXERCICE 01 ###############################

# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print (" O O O O O O ")
# def ham () :
#     print (" ============ ")

# bread()
# lettuce()
# tomato()
# ham()
# ham()
# bread()

############################ EXERCICE 02 ###############################

# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print (" O O O O O O ")
# def ham () :
#     print (" ============ ")
# def burger () :
#     bread()
#     lettuce()
#     tomato()
#     ham()
#     ham()
#     bread()

# for i in range(42):
#     burger()

############################ EXERCICE 03 ###############################

# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print (" O O O O O O ")
# def ham () :
#     print (" ============ ")
# def burger (number) :
#     for i in range(number):
#         bread()
#         lettuce()
#         tomato()
#         ham()
#         ham()
#         bread()

# number = int(input("How many sandwich do you need ? : "))

# if number < 0 :
#     print("Sorry i can't do that")
# else : 
#       burger(number)  

############################ EXERCICE 04 ###############################

def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print (" O O O O O O ")
def ham () :
    print (" ============ ")
def burger (number, vege) :
    if vege == "Y" or vege == "y" :
        for i in range(number):
            bread()
            lettuce()
            lettuce()
            tomato()
            tomato()
            bread()
    else :
        for i in range(number) :
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()

number = int(input("How many sandwich do you need ? : "))
vege = input("Do you want it to be vege ?(Y/N) : ")

if number < 0 :
    print("Sorry i can't do that")
else : 
      burger(number, vege)  
