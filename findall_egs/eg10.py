import re
txt="the rain in spain at 00:59"
x=re.findall("[0-5][0-9]",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
