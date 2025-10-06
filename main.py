# Import data from the projects different files
from add_passenger import AddPassenger
from remove_passenger import RemovePassenger
from show_passengers import ShowPassengers
from average_age import AverageAge
import json
import os

# Function to load passanger data from a JSON file
def load_json(filename):
    if not os.path.exists(filename):
        return []
        
    try:
        with open(filename, "r") as f:
            return json.load(f)
            
    except json.JSONDecodeError:
        return []

# Function to save passanger data into a JSON file
def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Function to display the meny and get user input
def show_menu():
    max_option = 4
    print("Welcome to python-bus")
    print("1. Add a passenger")
    print("2. Remove a passenger")
    print("3. Show all passengers")
    print("4. Show average age")
    print("0. Exit")
    
    while True:
        option = input("Answer: ")
        try:
            option = int(option)
            
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if 0 <= option <= max_option:
            return option
            
        else:
            print("Please enter a valid number")

# Main function that controls the program
def main():
    filename = "passengers.json"
    passengers = load_json(filename)
    
    # Create objects of our building blocks
    add_passenger = AddPassenger(passengers)
    remove_passenger = RemovePassenger(passengers)
    show_passengers = ShowPassengers(passengers)
    average_age = AverageAge(passengers)
    
    # Loop keeps program running until user chooses "Exit"
    while True:
        option = show_menu()
        if option == 1:
            add_passenger.Start()
            save_json(filename, passengers)
            
        elif option == 2:
            remove_passenger.Start()
            save_json(filename, passengers)
            
        elif option == 3:
            show_passengers.Start()
            
        elif option == 4:
            average_age.Start()
            
        elif option == 0:
            print("Exiting program")
            return

# Run the program only if this file is started directly (not imported)
if __name__ == "__main__":
    main()
