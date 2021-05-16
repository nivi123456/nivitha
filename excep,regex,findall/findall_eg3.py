#eg
import re
txt="hi nivitha"
x=re.findall("ni....a",txt)
print(x)
if x:
    print("yes we have match")
else:
    print("no match")
