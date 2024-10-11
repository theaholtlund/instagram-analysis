# Import required libraries
import os
from pathlib import Path
from bs4 import BeautifulSoup

# Function to get the directory of current script
def get_script_dir():
    """Returns the directory of the current script"""
    return os.path.dirname(os.path.realpath(__file__))

# Function to construct file path
def construct_file_path(*path_parts):
    """Constructs a file path from the given parts"""
    return Path(*path_parts)

# Function to list files in a directory and construct file path
def list_files_and_construct_paths(directory):
    """Lists files in a directory and constructs file paths"""
    directory = Path(directory)
    return [str(f) for f in directory.iterdir() if f.is_file()]

# Function to read file content
def read_file(file_path, as_lines=False):
    """Reads content from a file. Can return as a list of lines or a full string"""
    file_path = Path(file_path)
    with file_path.open("r", encoding="utf-8") as file:
        return file.readlines() if as_lines else file.read()

# Function to handle loading and parsing HTML content
def load_and_parse_html(file_path):
    """Loads and parses HTML content from a file using BeautifulSoup"""
    file_path = Path(file_path)
    with file_path.open("r", encoding="utf-8") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")

# Function to write analysis outputs to file
def write_to_file(file_path, data, header, detailed=False, data_label=None):
    """Writes data to a file, with optional headers and detailed formatting"""
    file_path = Path(file_path)
    with file_path.open("w", encoding="utf-8") as file:
        if detailed:
            file.write(f"{header}: {len(data)}\n")
            file.write(f"{data_label}:\n")
            for item in data:
                file.write(f"- {item}\n")
        else:
            if header:
                file.write(f"{header}")
            for item in data:
                file.write(f"{item}\n")

# Function to parse simple output file
def parse_simple_output(data):
    """Parses simple output file with a count in the first line"""
    header = data[0].strip()
    count = int(header.split(": ")[1])
    return count, []

# Function to parse list output file
def parse_list_output(data):
    """Parses list output file with items starting from the third line"""
    header = data[0].strip()
    count = int(header.split(": ")[1])
    items = [line.strip("- \n") for line in data[2:]]
    return count, items

# Function to parse detailed content output file
def parse_detailed_output(data):
    """Parses detailed output file with items after the first line"""
    header = data[0].strip()
    items = [line.strip("- \n") for line in data[1:] if line.strip()]
    return len(items), items
