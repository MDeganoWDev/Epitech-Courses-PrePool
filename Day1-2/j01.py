i = 1
x = 3
pi = 1

print("choisissez un nombre d'itération")
input = input()

while i <= int(input) :
    if  i%2 == 0:
        pi = pi - (4/x)
    else :
        pi = pi + (4/x)
    x = x+2
    i = i+1

print("pi est égale à : {0:.6f}".format(pi))
