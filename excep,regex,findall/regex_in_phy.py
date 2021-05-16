#RegEx in python
import re
txt="the rain in dgl"
x=re.search("^the.*dgl$",txt)
if x:
    print("yes we have the match")
else:
    print("no match")
