# Class to show passengers
class ShowPassengers:
    def __init__(self, passengers):
        # passengers is a list of dictionaries
        self.passengers = passengers

    # Method to print the passengers
    def Start(self):
        # if no passengers, print "No passengers"
        if not self.passengers:
            print("No passengers")
            return

        # If there are passengers, print the passengers
        print("Passengers:")        
        # Print each passenger with an id / # Display all passengers with their corresponding index
        for i, passenger in enumerate(self.passengers, start=1):
             # Print passenger details / # Use f-string to format the output with id and passenger info
             print(f"id: {i}, {passenger}")


if __name__ == "__main__":
    test_passengers = []
    test_passengers.append({"name": "Alice", "age": 20, "gender": "Female", "time": "10:00:00"})
    test_passengers.append({"name": "Bob", "age": 25, "gender": "Male", "time": "11:00:00"})

    # create object of ShowPassengers class and call Start method
    show_passengers = ShowPassengers(test_passengers)
    show_passengers.Start()
        
