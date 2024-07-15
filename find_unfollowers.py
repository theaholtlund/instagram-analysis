# Import required libraries
import os
from bs4 import BeautifulSoup

# Function to load HTML content with error handling
def load_html_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Please make sure you have copied the files into the 'instagram_data' folder.")
        exit()

# Specify the directory where Instagram data is expected to be placed
data_dir = "instagram_data"
connections_dir = "connections"
followers_dir = "followers_and_following"

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define paths for the HTML files within the data files folder
followers_path = os.path.join(script_dir, data_dir, connections_dir, followers_dir, "followers_1.html")
following_path = os.path.join(script_dir, data_dir, connections_dir, followers_dir, "following.html")

# Load the HTML content with error handling
followers_html = load_html_content(followers_path)
following_html = load_html_content(following_path)

# Parse the HTML content using BeautifulSoup
followers_soup = BeautifulSoup(followers_html, "html.parser")
following_soup = BeautifulSoup(following_html, "html.parser")

# Function to extract usernames from the provided HTML content
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Extract followers and following usernames
followers_usernames = extract_usernames(followers_soup)
following_usernames = extract_usernames(following_soup)

# Find account names the user is following, that are not following them back
not_following_back = following_usernames - followers_usernames

# Define output directory
output_dir = "analysis_outputs"

# Output the result to a file
output_file_path = os.path.join(script_dir, output_dir, "not_following_back.txt")
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write("Accounts not following back:\n")
    for username in not_following_back:
        output_file.write("- " + username + "\n")

# Print out confirmation of file export
print(f"Accounts not following back have been saved to '{output_file_path}'.")
