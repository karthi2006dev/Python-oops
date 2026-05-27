class Car:
    def __init__(self,name,year,color):
        self.name=name
        self.year=year
        self.color=color
    def description(self):
        print(f"Model:{self.name}")
        print(f"year:{self.year}")
        print(f"color:{self.color}")
    def start(self):
        print(f"{self.name} is started")
    def stop(self):
        print(f"{self.name} is stopped")
