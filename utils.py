# Import required libraries
import os
from bs4 import BeautifulSoup

# Function to load HTML content with error handling
def load_html_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: '{file_path}' not found. Please make sure you have added the data files to the project correctly.")

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
