import unittest
import tempfile
import numpy as np
import json
import os
from MonteCarloSim import MonteCarloSim
from file_reader import FileReader
from plotter import Plotter


class TestFileReader(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file for reading parameters
        self.test_file_path = 'testdocapi.txt'
        with open(self.test_file_path, 'w') as f:
            f.write("""Company: Apple Inc.
Ticker: AAPL-US
Industry: Telecommunication Equipment
Exchange: NASDAQ

Date: 2024/09/05

Monte Carlo Simulation Data:

S0: 100
mu: 0.08
sigma: 0.2
T: 1
num_steps: 252
""")

    def tearDown(self):
        # Remove the temporary test file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_read_parameters(self):
        # Test reading parameters from the file
        file_reader = FileReader(self.test_file_path)
        expected_params = {
            'S0': 100.0,
            'mu': 0.08,
            'sigma': 0.2,
            'T': 1.0,
            'num_steps': 252
        }

        params = file_reader.read_parameters()

        # Assert that the parameters read match the expected values
        self.assertEqual(params, expected_params)

    def test_save_json(self):
        # Test saving data as JSON to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            output_path = temp_file.name
            
        reader = FileReader("dummy_path")
        data = {'key': 'value'}
        reader.save_as_json(data, output_path)
        
        with open(output_path, 'r') as json_file:
            saved_data = json.load(json_file)
        
        # Assert that the saved JSON content matches the expected data
        self.assertEqual(saved_data, data)

        # Clean up the temporary JSON file
        os.remove(output_path)


class TestMonteCarloSim(unittest.TestCase):

    def test_simulate_paths(self):
        # Initialize parameters for the Monte Carlo simulation
        mcs = MonteCarloSim(S0=100, mu=0.05, sigma=0.2, T=1, num_simulations=1000, num_steps=100)
        paths = mcs.simulate_paths()

        # Check that the shape of the generated paths is correct
        self.assertEqual(paths.shape, (100, 1000))

        # Check that the initial value is correct
        self.assertAlmostEqual(paths[0, 0], 100)

        # Ensure the last row values are not all the same (simulation is varied)
        self.assertFalse(np.all(paths[-1, :] == paths[0, :]))
