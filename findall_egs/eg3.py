import re
txt="the rainssss in spain falls"
x=re.findall("inst",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
