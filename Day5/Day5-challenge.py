import random
import time

list = []
for i in range(1000000) :
    list.append(random.randint(0,10000000))
size = len(list)
position = [0]

for i in range(16):
    if i == 1:
        position.append(int(position[i]+size/16)-1)
        position.append(int(position[i]+size/16))
    elif i != size-1:
        position.append(int(position[i*2]+size/16))
    else :
        position.append(int(position[i*2]+size/16)-1)
        position.append(int(position[i*2]+size/16))

print(position)
 

# def sortingLoop(size, start):
#     while x < range:
#         if list[x] < list[x+1]:
#             list.insert(x, list[x+1])

# def spliting(list):
#     if len(list) < len(list)
#       start = len(list)/2
#       sortingLoop(start, start-1)
#       sortingLoop(start, start)


# startingTime = time.time()
# endTime = time.time()
# print(startingTime, endTime)
