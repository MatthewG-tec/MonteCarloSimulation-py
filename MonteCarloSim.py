import numpy as np

class MonteCarloSim:
    def __init__(self, S0, mu, sigma, T, num_simulations, num_steps):
        self.S0 = S0  # Initial stock price
        self.mu = mu  # Drift (expected return)
        self.sigma = sigma = sigma  # Volatility (std dev of returns)
        self.T = T  # Time period (in years)
        self.num_simulations = num_simulations  # Number of simulated paths
        self.num_steps = num_steps  # Number of time steps
        self.dt = T / num_steps  # Time step size
        
    def simulate_paths(self):
        # Initialize an array to store price paths
        paths = np.zeros((self.num_steps, self.num_simulations))
        paths[0] = self.S0  # Set the initial stock price for all paths
        
        # Simulate each path
        for t in range(1, self.num_steps):
            Z = np.random.standard_normal(self.num_simulations)  # Generate random values for Brownian Motion (Z ~ N(0, 1))
            # Update the price for the next time step using GBM
            paths[t] = paths[t - 1] * np.exp((self.mu - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z)
            
        return paths

    def calc_expected_final_price(self, paths):
        # Calculate the expected final price (mean of the paths)
        expected_price = np.mean(paths[-1, :])
        return expected_price