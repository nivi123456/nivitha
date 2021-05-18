import re
txt="the rain in spain"
x=re.findall("[^arn]",txt)
print(x)
if x:
    print("match")
else:
    print("no match")
