import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def plot_paths(self, paths):
        plt.figure(figsize=(12, 8))
        plt.plot(paths)
        plt.title('Simulated Stock Price Paths', fontsize = 16)
        plt.xlabel('Time Steps', fontsize = 14)
        plt.ylabel('Stock Price', fontsize = 14)
        # Add grid for better readability
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    def plot_histogram(self, paths, bin_size=0.25, bar_width=0.7):
        # Extract the final stock prices from all simulations
        final_prices = paths[-1, :]  # Last row contains the final prices
        
        # Create bins with size of $0.25
        min_price = np.min(final_prices)
        max_price = np.max(final_prices)
        bins = np.arange(min_price, max_price + bin_size, bin_size)
        
        # Plot the histogram
        plt.figure(figsize=(12, 8))  # Larger figure size for readability
        hist, edges = np.histogram(final_prices, bins=bins)

        # Calculate bin centers for plotting
        bin_centers = 0.5 * (edges[1:] + edges[:-1])

        # Plot using plt.bar() to control bar width
        plt.bar(bin_centers, hist, width=bar_width, edgecolor='black', color='skyblue', alpha=0.7)

        # Title and labels
        plt.title('Distribution of Final Stock Prices', fontsize=16)
        plt.xlabel('Stock Price (Binned in $0.25 intervals)', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)

        # Add grid for better readability
        plt.grid(True, linestyle='--', alpha=0.7)

        # Show plot
        plt.tight_layout()  # Ensure everything fits without overlapping
