import re

print("Choose a integer : ")
num = input()

if int(num) != 0:
    print("Choose a text : ")
    text = input()

    if int(num) <= 42 or len(re.findall("[aeiouy]", text)) != 0 :
        print(num)
    else :
        print(text)

