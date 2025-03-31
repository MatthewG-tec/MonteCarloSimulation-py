Monte Carlo Simulation for Stock Pricing Forecasting:
    - This project implements a Monte Carlo Simulation to forecast stock prices based
    on user-defined parameters. Reading input parameters from a txt file, and performs
    simulations, and visualizes the result.
-------------------------------------------------------------------------------------------------
    Structure:
    - main.py: Main script for reading parameters, simulation, and plotting.
    - MonteCarloSim.py: Contains the logic and class that handles the simulation. 
    - file_reader.py: Defines the class responsible for parsing through input parameters
    from a file and saving results to JSON.
    - plotter.py: Class for visualizing the simulated paths and their distribution (histogram)
    - MCS_Tests.py: Contains unit tests for FileReader and MonteCarloSim classes.

    Required Libraries:
    - Numpy, matplotlib, unittest
    - Can use "pip install numpy matplotlib plotter
-------------------------------------------------------------------------------------------------
Compiling:
    - Once Libraries are installed and python
    - python main.py (runs the whole program)
    - Visualizations are outputed one by one and can be saved.

Data:
    - Pulled from the FactSet data base.
    - Access through dhillon school of business student account.

** Does run on a standard terminal if python is installed and pip installed libraries
** If you want to run on IDE I used https://www.spyder-ide.org/ comes standard with all financial libraries
