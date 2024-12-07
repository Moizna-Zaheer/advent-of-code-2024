import re

# Function to read data from the file
def read_input_file(file_path):
    """
    Reads the content of the input file and returns it as a string.
    """
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()  # Read and remove surrounding whitespace
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return ""

# Function to compute the sum of products from valid mul(X,Y) instructions
def compute_sum_of_products(data):
    """
    Extracts valid 'mul(X,Y)' patterns from the input data and computes
    the sum of the products of X and Y.
    """
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    
    # Find all valid matches in the input
    matches = re.findall(pattern, data)
    
    # Compute the sum of the products
    return sum(int(x) * int(y) for x, y in matches)

# Main function to handle the process
def main():
    """
    Main function to read the file, process the data, and print the result.
    """
    # Input file path (change this to your actual file path)
    file_path = r"F:\Advent of Code\day3\problem3.txt"  # Replace with actual file path
    
    # Read the file content
    data = read_input_file(file_path)
    
    if data:  # If the file was read successfully
        # Compute the result
        result = compute_sum_of_products(data)
        
        # Print the result
        print(f"Total sum of multiplications: {result}")
    else:
        print("No valid input data to process.")

# Execute the main function
if __name__ == "__main__":
    main()
