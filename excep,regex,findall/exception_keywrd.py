#use exception keyword
try:
    a=int(input('enter a:'))
    b=int(input('enter b:'))
    c=a/b
    print("a/b=%d"%c)
except exception as e:
    print("can\'t divide by zero")
    print(e)
else:
    print("else block")
