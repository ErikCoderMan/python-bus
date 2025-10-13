class AverageAge:
    #Kontruktorn (_init_) körs när vi skapar objektet i main.py
    # Den tar in listan "passengers" (alla passangerare från JSON-filen)
    
    def __init__(self, passengers):
        self.passengers = passengers # Sparar listan på objektet så vi kan använda den senare
    
    # Metoden start körs när användaren väljer menyval 4 i main-filen
    def start(self):
        # Om det inte finns några passangerare alls, skriver ut sträng och avslutar.
        if not self.passengers:
            print("No passengers are on the bus.")
            return "No passengers are on the bus." # Return används för att möjliggöra pytest

        # Skapar tom lista för alla åldrar    
        ages = []
        for passenger in self.passengers: # Går igenom varje passangerare
            if "age" in passenger and passenger["age"] is not None: # Kollar att passangerare har en ålder
                ages.append(passenger["age"]) # Lägger till åldern i listan ages

        # Om ingen ålder på passangerare finns lagrad, skriver ut meddelande och avslutar.
        if not ages:
            print("No ages available for passengers.")
            return "No ages available for passengers." # Return används för pytest
        
        # Räknar ut medelåldern = summan av alla åldrar / antalet passangerare
        average = sum(ages)/len(ages)
        result = f"Average age of passengers is: {average:.1f} years"

        # Skriver ut genomsnittsåldern med en decimal
        print(result)
        return(result) # För Pytest att läsa och jämföra resultat
