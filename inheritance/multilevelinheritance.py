class Animal:
    def __init__(self, name):
        self.name = name

class Predator(Animal):
    pass
    def hunt(self):
       print(f"{self.name} is hunting")

class Prey(Animal):
    pass
    def run(self):
      print(f"{self.name} is running")

class Lion(Predator):
    pass
class Wolf(Predator):
    pass
class Deer(Prey):
    pass
class rabbit(Prey):
    pass

lion = Lion("Simbha");
deer= Deer("sambhar");

lion.hunt()
deer.run()
