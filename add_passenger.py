import datetime

class Passenger:
    def __init__(self, name: str, age: int, gender: str, time: str = None):
        self.name = name
        self.age = age
        self.gender = gender
        # Om ingen tid anges, använd nuvarande tid
        self.time = time or datetime.datetime.now().strftime("%H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "time": self.time
        }


class AddPassenger:
    def __init__(self, passengers):
        self.passengers = passengers

    def Start(self):
        print("Adding passenger")

        name = input("Name: ").strip()
        
        while True:
            age_input = input("Age: ").strip()
            if age_input.isdigit():
                age = int(age_input)
                break
            else:
                print("Please enter a valid number for age.")

        gender = input("Gender: ").strip()
        
        # Skapa en Passenger-objekt
        new_passenger = Passenger(name, age, gender)
        
        # Lägg till i listan "in place" som dict
        self.passengers.append(new_passenger.to_dict())
        print(f"Passenger {name} added successfully")


        
