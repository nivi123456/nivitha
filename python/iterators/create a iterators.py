#create a iterators
class myclass:
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
obj=myclass()
myiter=iter(obj)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
