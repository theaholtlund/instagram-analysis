# Import required libraries
import os
from bs4 import BeautifulSoup

# Function to get the directory of the current script
def get_script_dir():
    return os.path.dirname(os.path.realpath(__file__))

# Function to construct the file path
def construct_file_path(*path_parts):
    return os.path.join(*path_parts)

# Function to list files in a directory and construct the file path
def list_files_and_construct_paths(directory):
    file_paths = []
    for filename in os.listdir(directory):
        file_paths.append(os.path.join(directory, filename))
    return file_paths

# Function to read file content
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

# Function to handle loading and parsing HTML content
def load_and_parse_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")

# Function to write results to a file in simple format
def write_to_file_simple(file_path, data, header):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{header}: ")
        for item in data:
            file.write(f"{item}")

# Function to write results to a file in detailed format
def write_to_file_detailed(file_path, data, header, data_label):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{header}: {len(data)}\n")
        file.write(f"{data_label}:\n")
        for item in data:
            file.write(f"- {item}\n")

# Function to parse a simple output file
def parse_simple_output(data):
    header = data[0].strip()
    return int(header.split(": ")[1]), []

# Function to parse a list output file
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

# Function to capitalise only the first word
def capitalise_first_word(text):
    if not text:
        return text
    return text[0].upper() + text[1:].lower()
