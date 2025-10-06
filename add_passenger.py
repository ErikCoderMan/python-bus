
class AddPassenger:
    def __init__(self, name, age, gender, time):
        self.name = name
        self.age = age
        self.gender = gender
        self.time = time
    def __str__(self):
        return f"passenger(name: {self.name},age: {self.age}, gender: {self.gender}, added at {self.time})"
class bus:
    def __init__ (self, capacity = 10):
        self.capacity = capacity
        self.passengers = []


        
