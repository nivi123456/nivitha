#eg
import re
txt="the rain in dgl"
x=re.findall("[a-z]",txt)
print(x)
if x:
    print("yes we have match")
else:
    print("no match")
