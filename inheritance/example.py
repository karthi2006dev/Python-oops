class Animal:
    def __init__(self,name,isAlive):
        self.name=name;
        self.isAlive=isAlive;

class Dog(Animal):
 pass
 def describe(Animal):
      print(Animal.name)
      print(Animal.isAlive)
      print("WOOF")

class Cat(Animal):
 pass
 def describe(Animal):
       print(Animal.name)
       print(Animal.isAlive)
       print("MEOW")


cat1=Cat("cat","True")
dog1=Dog("dog","True")
cat1.describe()
dog1.describe()
