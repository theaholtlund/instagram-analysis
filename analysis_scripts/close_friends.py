# Import required libraries
import os
import sys

# Add the project root directory to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import the required modules
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file_detailed

# Function to extract usernames
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define path for the close friends HTML file
    close_friends_path = construct_file_path(script_dir, variables.data_dir, variables.connections_dir, variables.followers_dir, "close_friends.html")
    
    # Load and parse the HTML content
    close_friends_soup = load_and_parse_html(close_friends_path)
    
    # Extract close friends usernames
    close_friends_usernames = extract_usernames(close_friends_soup)
    
    # Output the result to a file
    output_file_path = construct_file_path(variables.output_dir, "close_friends.txt")
    write_to_file_detailed(output_file_path, close_friends_usernames, "Number of close friends", "Users on close friends list")
    
    # Print out confirmation of file export
    print(f"Close friends list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
