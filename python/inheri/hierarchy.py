#hierarchical inheritance
class base():
    def func1(host):
        print("base class function")
class derived1(base):
    def func2(host):
        print("derived 1 class function")
class derived2(base):
    def func3(host):
        print("derived 2 class function")
obj=derived1()
obj1=derived2()

obj.func1()
obj.func2()

obj1.func1()
obj1.func3()
