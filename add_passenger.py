import datetime

class AddPassenger:
    def __init__(self, passengers):
        self.passengers = passengers
    def Start(self):
        print("Add passenger")
        try:
            name = input("Name:  ").strip()
            while True:
                age_input = input("Age:  ").strip()
                if age_input.isdigit():
                    age = int(age_input)
                    break
                else:
                    print("Enter a valid number")
            gender = input("Gender:  ").strip()
            time = datetime.datetime.now().strftime("%H:%M:%S")
            new_person ={
                "name": name,
                "age": age,
                "gender": gender,
                "time": time
                    }
            self.passengers.append(new_person)
            print(f"Passenger {name} added!")
        except Exception as e:
            print(f"Error: {e}")
        
