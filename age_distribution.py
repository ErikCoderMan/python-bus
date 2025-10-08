import matplotlib.pyplot as plt

class AgeDistribution:
    def __init__(self, passengers):
        self.passengers = passengers

    def show_age_distribution(self):
        if not self.passengers:
            print("No passengers to show.")
            return

        # Hämta alla åldrar ur listan
        ages = [p["age"] for p in self.passengers if "age" in p]

        # Skapa ett histogram
        plt.figure(figsize=(8, 5))
        plt.hist(ages, bins=range(0, 101, 10), edgecolor='black', alpha=0.7)

        # Sätt x-ticksen på 10, 20, … 100
        plt.xticks(range(10, 101, 10))

        plt.title("Age Distribution of Passengers")
        plt.xlabel("Age")
        plt.ylabel("Number of Passengers")
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()

        # Visa grafen
        plt.show()
