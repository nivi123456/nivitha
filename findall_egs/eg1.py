import re
txt="hello world"
x=re.findall("^hello",txt)
if x:
    print("match")
else:
    print("no match")
