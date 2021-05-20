import re
x="the rain in spain"
x=re.search("\s",x)
print("the first white space character is loacted in position:",x.start())
