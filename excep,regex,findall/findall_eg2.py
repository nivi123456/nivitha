import re
txt="that will be 59 dollars"
x=re.findall("\d",txt)
print(x)
if x:
    print("yes we have match")
else:
    print("no match")
