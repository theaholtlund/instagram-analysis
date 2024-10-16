# Import required libraries
import os
import sys

# Add project root directory to system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file

# Function to extract usernames
def extract_usernames(soup):
    """Extract usernames from HTML content."""
    return {a.text for a in soup.find_all("a", href=True)}

def main():
    """Extract close friends from HTML and save to text file."""
    script_dir = get_script_dir()
    
    # Load, parse and extract close friends accounts from HTML content
    close_friends_path = construct_file_path(script_dir, variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR, variables.CLOSE_FRIENDS_FILE)
    close_friends_soup = load_and_parse_html(close_friends_path)
    close_friends_usernames = extract_usernames(close_friends_soup)
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "close_friends.txt")
    write_to_file(output_file_path, close_friends_usernames, "Number of close friends", detailed=True, data_label="Users on close friends list")
    print(f"Close friends list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
