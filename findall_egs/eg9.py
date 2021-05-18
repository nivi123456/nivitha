import re
txt="the rain in spain at 04.00pm"
x=re.findall("[0-9]",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
