class RemovePassenger:
    def __init__(self, passengers):
        self.passengers = passengers # this list will be changed "in place"
        
    def Start(self):
        # show list with index
        for i, passenger in enumerate(self.passengers):
            print(f"id: {i}, {passenger}")
        
        # ask for what index to remove
        try:
            answer = int(input("Enter id to remove: "))
            if 0 <= answer < len(self.passengers):
                removed = self.passengers.pop(answer)
                print(f"Removed: {removed}")
                
            else:
                print("Invalid id")
                
        except ValueError:
            print("Please enter a number")
        
        # newline
        print("")
