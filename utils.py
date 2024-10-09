# Import required libraries
import os
from pathlib import Path
from bs4 import BeautifulSoup

# Function to get the directory of current script
def get_script_dir():
    return os.path.dirname(os.path.realpath(__file__))

# Function to construct file path
def construct_file_path(*path_parts):
    return Path(*path_parts)

# Function to list files in a directory and construct file path
def list_files_and_construct_paths(directory):
    directory = Path(directory)
    return [str(f) for f in directory.iterdir() if f.is_file()]

# Function to read file content
def read_file(file_path, as_lines=False):
    file_path = Path(file_path)
    with file_path.open("r", encoding="utf-8") as file:
        return file.readlines() if as_lines else file.read()

# Function to handle loading and parsing HTML content
def load_and_parse_html(file_path):
    file_path = Path(file_path)
    with file_path.open("r", encoding="utf-8") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")

# Function to write analysis outputs to file
def write_to_file(file_path, data, header, detailed=False, data_label=None):
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
    header = data[0].strip()
    count = int(header.split(": ")[1])
    return count, []

# Function to parse list output file
def parse_list_output(data):
    header = data[0].strip()
    count = int(header.split(": ")[1])
    items = [line.strip("- \n") for line in data[2:]]
    return count, items

# Function to parse detailed content output file
def parse_detailed_output(data):
    header = data[0].strip()
    items = [line.strip("- \n") for line in data[1:] if line.strip()]
    return len(items), items
