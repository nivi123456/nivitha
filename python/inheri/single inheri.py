#single inheritance
#base class
class parent:
    def func1(host):
        print("this function is in parent class")
#derived class
class child(parent):
    def func2(host):
        print("this function is in child class")
#driver's code
obj=child()
obj.func1()
obj.func2()
