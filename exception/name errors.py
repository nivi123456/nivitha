try:
    print(x)
    x=9
    y=0
    print(x/y)
except NameError:
    print("variable x is not defined")
except:
    print("other errors")
