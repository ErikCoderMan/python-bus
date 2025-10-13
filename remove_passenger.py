class RemovePassenger:
    def __init__(self, passengers):
        # Store the list of passengers. This list will be modified "in place".
        self.passengers = passengers
        
    def start(self):
        """
        This method is called from main.py to remove a passenger
        from the list based on its index.
        """
        
        try:
            # Ask the user to enter the index of the passenger to remove
            answer = int(input("Enter id to remove: "))
            
            # Check if the entered index is within the valid range
            if 1 <= answer <= len(self.passengers):
                # Remove the passenger at the given index
                removed = self.passengers.pop(answer-1)
                print(f"Removed passenger: {removed}")
                
            else:
                # Index is out of bounds
                print("Invalid id, please enter a number within the list range.")
                
        except ValueError:
            # Handle the case where input is not a number
            print("Invalid input, please enter a numeric value.")

        # Print a blank line for spacing
        print("")
