class AverageAge:
    # Metoden init importerar in listan "passengers" med passangerare från JSON-filen
    def __init__(self, passengers):
        self.passengers = passengers # Sparar listan på objektet så vi kan använda den senare
    
    # Metoden start körs när användaren väljer menyval 4 i main-filen
    def start(self):
        # Kontrollerar ifall listan med passangerare är tom, om ja skrivs "No passengers on the bus" ut
        if not self.passengers:
            print("No passengers are on the bus.")
            return "No passengers are on the bus." # Return används för att möjliggöra pytest

        # Om passagerare hittas, skapas tom lista för alla åldrar    
        ages = []
        for passenger in self.passengers: # Program går igenom varje passangerare i listan, kollar att den har en ålder och lägger till i listan ages
            if "age" in passenger and passenger["age"] is not None: #
                ages.append(passenger["age"]) # Lägger till åldern i listan ages

        # Om ingen ålder på passangerare finns lagrad, skriver ut meddelande och avslutar
        if not ages:
            print("No ages available for passengers.")
            return "No ages available for passengers." # Return används för pytest
        
        # Om det finns åldrar i listan: Summan av alla åldrar / antalet passangerare
        average = sum(ages)/len(ages)
        result = f"Average age of passengers is: {average:.1f} years" # Medelåldern sparas i variabeln result och formateras med en decimal med f-string

        # Skriver ut genomsnittsåldern med en decimal
        print(result)
        return(result) # För Pytest att läsa och jämföra resultat
