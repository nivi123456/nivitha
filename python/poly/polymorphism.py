#polymorphism
class potato:
    def type(host):
        print("vegetable")
    def color(host):
        print("golden brown")
class mango:
    def type(host):
        print("fruit")
    def color(host):
        print("yellow")
def func(obj):
    obj.type()
    obj.color()
    
obj_po=potato()
obj_ma=mango()

func(obj_po)
func(obj_ma)
