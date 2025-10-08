class AverageAge:
    #Kontruktorn (_init_) körs när vi skapar objektet i main.py
    # Den tar in listan "passengers" (alla passangerare från JSON-filen)
    
    def __init__(self, passengers):
        self.passengers = passengers # Sparar listan på objektet så vi kan använda den senare
    
    # Metoden start körs när användaren väljer menyval 4 i main-filen
    def Start(self):
        # Om det inte finns några passangerare alls, skriver ut sträng och avslutar.
        if not self.passengers:
            print("No passengers are on the bus.")
            return

        # Skapar tom lista för alla åldrar    
        ages = []
        for passenger in self.passengers: # Går igenom varje passangerare
            if "age" in passenger: # Kollar att passangerare har en ålder
                ages.append(passenger["age"]) # Lägger till åldern i listan ages

        # Om ingen har ålder lagrad, skriver ut meddelande och avslutar.
        if not ages:
            print("No ages available for passengers.")
            return
        
        # Räknar ut medelåldern = summan av alla åldrar/antalet passangerare
        average = sum(ages)/len(ages)
        # Skriver ut genomsnittsåldern med en decimal
        print(f"Average age of passengers is: {average:.1f} years")