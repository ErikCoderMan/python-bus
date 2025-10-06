class ShowPassengers:
    def __init__(self, passengers):
        self.passengers = passengers

    def Start(self):
        if not self.passengers:
            print("No passengers")
            return
        print("Passengers:")
        for passenger in self.passengers:
            print("-", passenger)


if __name__ == "__main__":
            ShowPassengers(["Alice","Bob","Charlie"]).Start()
        
