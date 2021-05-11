#to stop the iteration
class myclass:
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        if(self.a<=10):
            x=self.a
            self.a+=1
            return x
        else:
            raise stopiteration
obj=myclass()
myiter=iter(obj)
for x in myiter:
    print(x)
