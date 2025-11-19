###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

# -----------------------------------------
# Import dependencies with error handling
# -----------------------------------------
try:
    import numpy as np
except ImportError:
    raise ImportError("NumPy is required for statistics.py. Install it using 'pip install numpy'.")

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib is required for histogram plotting. Install with 'pip install matplotlib'.")
    

# -----------------------------------------
# Helper: validate input
# -----------------------------------------
def _ensure_array(data):
    """
    Ensure the input is a numpy array.
    Convert list -> numpy array.
    Raise error otherwise.
    """
    if isinstance(data, np.ndarray):
        return data
    elif isinstance(data, list):
        return np.array(data)
    else:
        raise TypeError("Input data must be a list or numpy array.")

# -----------------------------------------
# Basic statistics
# -----------------------------------------
def mean(data):
    """Calculate the mean of the data."""
    arr = _ensure_array(data)
    return np.mean(arr)

def median(data):
    """Calculate the median of the data."""
    arr = _ensure_array(data)
    return np.median(arr)

def std(data):
    """Calculate the standard deviation."""
    arr = _ensure_array(data)
    return np.std(arr)


# -----------------------------------------
# Pretty printing
# -----------------------------------------
def pretty_print_stats(data):
    """Print mean, median, std in a clean format."""
    arr = _ensure_array(data)
    m = mean(arr)
    med = median(arr)
    s = std(arr)

    print("=== Summary Statistics ===")
    print(f"Mean:   {m:.4f}")
    print(f"Median: {med:.4f}")
    print(f"Std:    {s:.4f}")
    print("==========================")


# -----------------------------------------
# Histogram plotting (with mean & median lines)
# -----------------------------------------
def plot_histogram(data, bins=20):
    """
    Plot a histogram of the data, marking mean & median.
    """
    arr = _ensure_array(data)
    m = mean(arr)
    med = median(arr)

    plt.hist(arr, bins=bins, alpha=0.7, edgecolor="black")
    plt.axvline(m, color="red", linestyle="--", linewidth=2, label=f"Mean = {m:.2f}")
    plt.axvline(med, color="blue", linestyle="--", linewidth=2, label=f"Median = {med:.2f}")

    plt.title("Histogram with Mean & Median")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

# -------------------------
# function to read data from file
# -------------------------

def read_data_from_file(file_path):
    """
    Reads numbers from a text or CSV file and returns a numpy array.
    Assumes numbers are separated by commas, spaces, or newlines.
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Split by commas, spaces, or newlines
        import re
        numbers = re.split(r"[,\s]+", content.strip())

        # Convert to floats
        data = [float(x) for x in numbers if x != '']
        return _ensure_array(data)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except ValueError:
        print("File contains non-numeric data.")
        return None
    except Exception as e:
        print("Error reading file:", e)
        return None


# -------------------------
# function to prompt user for input -- user either enters data manually or reads from a file
# -------------------------

def run_statistics():
    """
    Interactive interface for user to input data or read from a file.
    """
    print("Statistics Tool")
    print("1. Enter data manually")
    print("2. Read data from a file")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Choose an option (1, 2, exit): ").strip().lower()
        if choice == "exit":
            print("Exiting statistics tool.")
            break

        if choice == "1":
            user_input = input("Enter your data as numbers separated by commas: ")
            try:
                data = [float(x) for x in user_input.split(",")]
                arr = _ensure_array(data)
            except Exception as e:
                print("Error:", e)
                continue

        elif choice == "2":
            file_path = input("Enter the path to your data file: ").strip()
            arr = read_data_from_file(file_path)
            if arr is None:
                continue  # error reading file, retry

        else:
            print("Invalid choice. Try again.\n")
            continue

        # Print stats and plot
        pretty_print_stats(arr)
        plot_histogram(arr)

if __name__ == "__main__":
    run_statistics()