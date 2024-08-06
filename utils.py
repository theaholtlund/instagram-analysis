# Import required libraries
import os
from bs4 import BeautifulSoup

# Function to get the directory of the current script
def get_script_dir():
    """
    Get the directory of the current script.

    Returns:
        str: The directory path of the current script.
    """
    return os.path.dirname(os.path.realpath(__file__))

# Function to read file content
def read_file(file_path, mode):
    """
    Read content from a file.

    Args:
        file_path (str): The path to the file.
        mode (str): The mode to read the file ('all' for full content, 'lines' for line by line).

    Returns:
        str or list: The file content or list of lines.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            if mode == "all":
                return file.read()
            elif mode == "lines":
                return file.readlines()
            else:
                raise ValueError(f"Invalid mode: {mode}. Use 'all' or 'lines'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be found.")
        return None

# Function to write results to a file in simple format
def write_to_file_simple(file_path, data, header):
    """
    Write data to a file in a simple format.

    Args:
        file_path (str): The path to the output file.
        data (list): The data to write.
        header (str): The header for the output.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{header}: ")
        for item in data:
            file.write(f"{item}")

# Function to write results to a file in detailed format
def write_to_file_detailed(file_path, data, header, data_label):
    """
    Write data to a file in a detailed format.

    Args:
        file_path (str): The path to the output file.
        data (list): The data to write.
        header (str): The header for the output.
        data_label (str): The label for the data section.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{header}: {len(data)}\n")
        file.write(f"{data_label}:\n")
        for item in data:
            file.write(f"- {item}\n")

# Function to parse a simple output file
def parse_simple_output(data):
    """
    Parse the output of a simple format file.

    Args:
        data (list): The list of lines from the file.

    Returns:
        tuple: A tuple containing the count and an empty list (no items in simple output).
    """
    header = data[0].strip()
    return int(header.split(": ")[1]), []

# Function to parse a list output file
def parse_list_output(data):
    """
    Parse the output of a list format file.

    Args:
        data (list): The list of lines from the file.

    Returns:
        tuple: A tuple containing the count and list of items.
    """
    header = data[0].strip()
    count = int(header.split(": ")[1])
    items = [line.strip("- \n") for line in data[2:]]
    return count, items

# Function to parse detailed content output file
def parse_detailed_output(data):
    """
    Parse the output of a detailed format file.

    Args:
        data (list): The list of lines from the file.

    Returns:
        tuple: A tuple containing the count and list of items.
    """
    header = data[0].strip()
    items = [line.strip("- \n") for line in data[1:] if line.strip()]
    return len(items), items

# Function to capitalise only the first word
def capitalise_first_word(text):
    """
    Capitalise only the first word of a string.

    Args:
        text (str): The input text.

    Returns:
        str: The text with the first word capitalised.
    """
    if not text:
        return text
    return text[0].upper() + text[1:].lower()
