import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad

def plot_probability_area(mean, std_dev, a, b):
    """
    Plots the PDF of a normal distribution and shades the area between a and b.

    Parameters:
    - mean: Mean of the normal distribution
    - std_dev: Standard deviation of the normal distribution
    - a: Start of the interval
    - b: End of the interval
    """

    # Define the PDF using scipy's norm
    pdf = lambda x: norm.pdf(x, loc=mean, scale=std_dev)

    # Calculate the probability (area under the curve) between a and b
    area, _ = quad(pdf, a, b)

    # Generate values for plotting
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = pdf(x)

    # Values for the shaded area
    x_fill = np.linspace(a, b, 1000)
    y_fill = pdf(x_fill)

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="Probability Density", color="blue")
    plt.fill_between(x_fill, y_fill, color="lightgreen", alpha=0.6,
                     label=f"P({a} < X < {b}) ≈ {area:.4f}")
    plt.title("Probability as Area Under the Curve")
    plt.xlabel("x (e.g., Time in seconds)")
    plt.ylabel("Probability Density (1/unit)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Print the result
    print(f"Probability that X is between {a} and {b}: {area:.4f}")
