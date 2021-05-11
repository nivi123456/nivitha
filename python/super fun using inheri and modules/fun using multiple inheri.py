#super function using multiple inheritance
class mammal():
    def __init__(self,name):
        print(name,"is a mammal")
class canFLY(mammal):
    def __init__(self,canFLY_name):
        print(canFLY_name,"cannot FLY")
        super().__init__(canFLY_name)
class canswim(mammal):
    def __init__(self,canswim_name):
        print(canswim_name,"cannot swim")
        super().__init__(canswim_name)
class animal(canFLY,canswim):
    def __init__(self,name):
        super().__init__(name)
carol=animal("dog")
