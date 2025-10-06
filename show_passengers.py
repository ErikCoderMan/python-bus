class ShowPassengers:
    def __init__(self, passengers):
        self.passengers = passengers

    def Start(self):
        if not self.passengers:
            print("No passengers")
            return
        print("Passengers:")
        for passenger in self.passengers:
            print(passenger)


if __name__ == "__main__":
            test_passengers = []
            test_passengers.append({"name": "Alice", "age": 20, "gender": "Female", "time": "10:00:00"})
            test_passengers.append({"name": "Bob", "age": 25, "gender": "Male", "time": "11:00:00"})

            # create object of ShowPassengers class and call Start method
            show_passengers = ShowPassengers(test_passengers)
            show_passengers.Start()
        
