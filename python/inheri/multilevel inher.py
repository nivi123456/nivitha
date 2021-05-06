#multilevel inheritance
class animal():
    def eat(host):
        print("eating.....")
class dog(animal):
    def bark(host):
        print("barking.....")
class puppy(dog):
    def weep(host):
        print("weeping....")
obj=puppy()
obj.eat()
obj.bark()
obj.weep()
