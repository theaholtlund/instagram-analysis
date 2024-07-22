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

# Function to write results to a file
def write_to_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Number of blocked accounts: {len(data)}\n")
        file.write("Blocked accounts:\n")
        for username in data:
            file.write(f"- {username}\n")