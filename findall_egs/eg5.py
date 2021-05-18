import re
txt="the rain in spain falls mainly in july to sept"
x=re.findall("nivitha/neela",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
