import matplotlib.pyplot as plt
import numpy as np

# Create x values from -10 to 10
x = np.linspace(-3, 3, 400)

# Compute y values for the equation y = x^2 - 4
y= (3*(x**2))/(x**2 -4)
# Plot
plt.plot(x, y, label="y = (3x²)/(x² - 4)", color="blue")
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.title("Graph of y = (3x²)/(x² - 4)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
