#multiple inheritance
class calc1:
    def summation(host,x,y):
        return x+y
class calc2:
    def product(host,x,y):
        return x*y
class derived(calc1,calc2):
    def subtraction(host,x,y):
        return x-y
obj=derived()
print(obj.summation(95,100))
print(obj.product(88,90))
print(obj.subtraction(100,6))
