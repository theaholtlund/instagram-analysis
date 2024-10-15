# Import required libraries
import os
from pathlib import Path
from bs4 import BeautifulSoup

# Function to get the directory of current script
def get_script_dir():
    """Return the directory of the current script."""
    return os.path.dirname(os.path.realpath(__file__))

# Function to construct file path
def construct_file_path(*path_parts):
    """Construct a file path from the given parts."""
    return Path(*path_parts)

# Function to list files in a directory and construct file path
def list_files_and_construct_paths(directory):
    """List files in a directory and construct their full paths."""
    directory = Path(directory)
    return [str(f) for f in directory.iterdir() if f.is_file()]

# Function to read file content
def read_file(file_path, as_lines=False):
    """Read content from a file, returning either a string or list of lines."""
    file_path = Path(file_path)
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return file.readlines() if as_lines else file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to handle loading and parsing HTML content
def load_and_parse_html(file_path):
    """Load and parse HTML content from a file using BeautifulSoup."""
    file_path = Path(file_path)
    try:
        with file_path.open("r", encoding="utf-8") as file:
            html_content = file.read()
        return BeautifulSoup(html_content, "html.parser")
    except Exception as e:
        print(f"Error parsing HTML file {file_path}: {e}")
        return None

# Function to write analysis outputs to file
def write_to_file(file_path, data, header="", detailed=False, data_label=None):
    """Write data to a file, with optional headers and detailed formatting."""
    file_path = Path(file_path)
    try:
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
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

# Function to parse simple output file
def parse_simple_output(data):
    """Parse a simple output file with a count in the first line"""
    header = data[0].strip()
    count = int(header.split(": ")[1])
    return count, []

# Function to parse list output file
def parse_list_output(data):
    """Parse list output file with items starting from the third line."""
    header = data[0].strip()
    count = int(header.split(": ")[1])
    items = [line.strip("- \n") for line in data[2:]]
    return count, items

# Function to parse detailed content output file
def parse_detailed_output(data):
    """Parse detailed output file with items after the first line."""
    header = data[0].strip()
    items = [line.strip("- \n") for line in data[1:] if line.strip()]
    return len(items), items
