import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\REHAN KHAN\Documents\Book1.csv")

print(data)

# Line plot
plt.figure()
plt.plot(data["years"], data["sales"])
plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Yearly Sales Growth")
plt.show()

# Bar chart
plt.figure()
plt.bar(data["Year"], data["Sales"])
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Yearly Sales Bar Chart")
plt.show()

