from MonteCarloSim import MonteCarloSim
from file_reader import FileReader
from plotter import Plotter
import MCS_Tests
import unittest
from pathlib import Path

if __name__ == "__main__":
    
    # Use dynamic paths to find the file if downloaded onto another system
    base_path = Path.cwd()
    
    # Function for pulling data variables needed for simulation.
    file_path = base_path / 'DataParse.txt'
    json_output_path = base_path / 'output.json'
    
    # Read input parameters from 'DataParse.txt'
    file_reader = FileReader(file_path)
    params = file_reader.read_parameters()
    
    if params:
        S0 = params['S0']
        mu = params['mu']
        sigma = params['sigma']
        T = params['T']
        num_steps = params['num_steps']
        num_simulations = 10000  # Define the number of simulations manually can be increased if want more price paths
        
        # Save parameters to JSON
        file_reader.save_as_json(params, json_output_path)
        
        # Running Monte Carlo Simulation
        mcs = MonteCarloSim(S0, mu, sigma, T, num_simulations, num_steps)
        simulated_paths = mcs.simulate_paths()
        
        # Calculate expected final price
        expected_final_price = mcs.calc_expected_final_price(simulated_paths)
        print(f"Most likely ending price (expected final price): {expected_final_price:.2f}")
        
        # Plot the price path simulation
        plotter = Plotter()
        plotter.plot_paths(simulated_paths)  # First plot: price path simulation
        
        # Plot the histogram
        plotter.plot_histogram(simulated_paths, bin_size=0.25)  # Second plot: histogram
    
    # Ensure that the plots are fully rendered and closed before running tests
    import matplotlib.pyplot as plt
    plt.show(block=True)  # This ensures all open plots are rendered and finished
    
    # Run tests after all plots
    print("\nRunning tests...")
    suite = unittest.defaultTestLoader.loadTestsFromModule(MCS_Tests)
    unittest.TextTestRunner().run(suite)
