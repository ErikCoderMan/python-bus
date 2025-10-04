class AverageAge:
    #Kontruktorn (_init_) körs när vi skapar objektet i main.py
    # Den tar in listan "passengers" (alla passangerare från JSON-filen)
    
    def __init__(self, passengers):
        self.passengers = passengers # Sparar listan på objektet så vi kan använda den senare

    def Start(self):
        if not self.passengers:
            print("No passengers are on the bus.") # Skriver ut meddelande om att det inte finns några passangerare på bussen och avslutar.
            return

        # Skapar tom lista för alla åldrar    
        ages = []
        for passenger in self.passengers:
            if "age" in passenger:
                ages.append(passenger["age"])

        # Om ingen har ålder lagrad, skriver ut meddelande och avslutar.
        if not ages:
            print("No ages available for passengers.")
            return