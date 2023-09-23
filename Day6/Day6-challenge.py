import time

n1 = 48
n2 = 84
n3 = 168

def calc (number, power) :
    if power > 1 :
        number *= calc(number, power - 1)
    return number

start = time.time()
calc(n1, n2)
end = time.time() - start
print("\nDURATION ", n2, ": %.6f seconds\n\n" % end)

start = time.time()
calc(n1, n3)
end = time.time() - start
print("\nDURATION ", n3, " : %.6f seconds\n\n" % end)
#  test