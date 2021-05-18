import re
txt="the rain in spain falls"
x=re.findall("aix*",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
