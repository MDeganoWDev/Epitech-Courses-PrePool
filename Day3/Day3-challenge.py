mot= "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
mot2= mot[::-1]
result= 0

if mot.find("cat"):
    result += 1
if mot2.find("cat"):
    result += 1
if mot.find("garden"):
    result += 1
if mot.find("mice"):
    result += 1

print(result)