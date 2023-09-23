############################ EXERCICE 01 ###############################
#
vip = {
    "name" : {
        "toto",
        "tata",
        "titi",
        "tete",
        "tutu"
    }
}
names = vip["name"]
worth = False
input = input("Exercice 1 : Quelle est votre nom ? : ")

for name in names :
    if input == name :
        worth = True
        break

if worth :
    print("Exercice 1 : Welcome in !")
else :
    print("Exercice 1 : Get lost !")
worth = False

############################ EXERCICE 02 ###############################
#
vip = {
    "name" : {
        "toto",
        "tutu",
        "tata",
        "tata",
        "tutu",
        "tata",
        "titi",
        "tete",
        "tete",
        "tutu"
    }
}
names = vip["name"]
for name in names :
    count = 0
    for entry in names:
        if name == entry: 
            if count > 0:
                names.remove(entry)
            else: 
                count +- 1
        
print("Exercice 2 :", names)
############################ EXERCICE 03 ###############################
# 
meeting1 = {
    "day" : "Monday",
    "hour" : "14pm",
    "employe" : {
        "toto",
        "titi",            
    },
}
meeting2 = {
    "day" : "Thursday",
    "hour" : "14pm",
    "employe" : {       
        "tata",
        "titi",
        "tutu",         
    },
}
meeting3 = {
    "day" : "Wensday",
    "hour" : "14pm",
    "employe" : {
        "titi",
        "tutu",
        "tete",            
    },
}
meeting4 = {
    "day" : "Sunday",
    "hour" : "14pm",
    "employe" : {
        "toto",
        "tata",       
    },
}
meeting5 = {
    "day" : "Monday 2",
    "hour" : "14pm",
    "employe" : {
        "toto",
        "titi",
        "tutu",          
    },
}
meetings = [meeting1, meeting2, meeting3, meeting4, meeting5]
result = ""
# search = "toto"
search = input("Exercice 3 : Qui cherchez vous ? : ")

for meeting in meetings:
    for name in meeting["employe"]:
        if name == search:
            result += meeting["day"]+" "
print("Exercice 3 : ", search, " is in ", result, " meetings.")

