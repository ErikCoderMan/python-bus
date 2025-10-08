import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class AgeDistribution:
    def __init__(self, passengers):
        self.passengers = passengers

    def show_age_distribution(self):
        if not self.passengers:
            print("No passengers to show.")
            return

        # Gather all ages from the list of passengers
        ages = [p["age"] for p in self.passengers if "age" in p]

        # Create a histogram
        plt.figure(figsize=(8, 5))
        max_age = max(ages)
        bins = range(0, (max_age // 10 + 2) * 10, 10)
        plt.hist(ages, bins=bins, edgecolor='black', alpha=0.7)
        ax = plt.gca()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        # Set ticks to 10, 20, … 100
        plt.xticks(bins)

        plt.title("Age Distribution of Passengers")
        plt.xlabel("Age")
        plt.ylabel("Number of Passengers")
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        # Show histogram
        plt.show()
