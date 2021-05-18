import re
txt="the rain in spain falls mainly in july to sept"
x=re.findall("al{3}",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
