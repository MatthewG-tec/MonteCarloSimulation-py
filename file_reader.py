import json

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_parameters(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.readlines()
                
            params = {}
            parameter_section = False
            
            for line in data:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # Check start of the parameters
                if "Monte Carlo Simulation Data:" in line:
                    parameter_section = True
                    continue  # Skip this line
                
                if parameter_section:
                    parts = line.split(':')
                    if len(parts) != 2:  # Ensure format 'key: value'
                        print(f"Ignored line (invalid format): {line}")
                        continue  # Ignore invalid lines

                    key = parts[0].strip()  # Remove whitespace from key
                    value = parts[1].strip()  # Remove whitespace from value
                    
                    # Only process expected data
                    if key == "S0":
                        params['S0'] = float(value)  # Initial stock price
                    elif key == "mu":
                        params['mu'] = float(value)  # Drift (expected return) assuming a value between 3% and 5%
                    elif key == "sigma":
                        params['sigma'] = float(value)  # Volatility 
                    elif key == "T":
                        params['T'] = float(value)  # Time period (1 year)
                    elif key == "num_steps":
                        params['num_steps'] = int(value)  # Number of steps (252 as there are that many trading days)

            print(f"Extracted parameters: {params}")
            return params

        except FileNotFoundError:
            print(f"The file '{self.file_path}' does not exist.")
        except IOError:
            print(f"An error occurred while reading the file '{self.file_path}'.")
        return None
  
    def save_as_json(self, data, output_path):
        try:
            # Save JSON data to file to make sure used data is saved
            with open(output_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"\nJSON data successfully written to '{output_path}'.")
        
        except FileNotFoundError:
            print(f"The file '{output_path}' does not exist.")
        except IOError:
            print(f"An error occurred while writing the file '{output_path}'.")
