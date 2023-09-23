print("Choisissez un nombre d'itération")
i = int(input())
x = 3
pi = 1

while i != 0:
    pi = pi/6+(x*x/6)
    x = x+2
    i = i-1

pi = pi + 3
print("pi est égale à : {0:.6f}".format(pi))

# non fini