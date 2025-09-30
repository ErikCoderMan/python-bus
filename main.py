from add_passenger import AddPassenger
from remove_passenger import RemovePassenger
from show_passengers import ShowPassengers
from average_age import AverageAge

def show_menu():
    max_option=4
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
        
        except Exception as e:
            print("Please enter a valid number")
            continue
        
        if 0 <= option <= max_option:
            return option
        
        else:
            print("Please enter a valid number")
            continue

def main():
    # list that will be passed as parameter to other classes, it will be updated in place
    passengers = []
    
    # create objects
    add_passenger = AddPassenger()
    remove_passenger = RemovePassenger()
    show_passengers = ShowPassengers()
    average_age = AverageAge()
    
    # while loop that runs until user selects option 0
    while True:
        option = show_menu()
        if option == 1:
            add_passenger.Start(passengers) # method edits list
        
        elif option == 2:
            remove_passenger.Start(passengers) # method edits list
        
        elif option == 3:
            show_passengers.Start(passengers) # method prints out list
            
        elif option == 4:
            average_age.Start(passengers) # method prints sum divided by list length
        
        elif option == 0:
            print("Exiting program")
            return
    
if __name__ == "__main__":
    main()
        
        
        
