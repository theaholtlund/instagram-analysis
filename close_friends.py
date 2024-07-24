# Import required libraries
import os
from bs4 import BeautifulSoup
import config
from utils import load_html_content, write_to_file_detailed, create_output_dir, get_script_dir

# Function to extract usernames from the provided HTML content
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Main function to coordinate execution of the script
def main():
    # Get the directory of the current script
    script_dir = get_script_dir()
    
    # Define path for the close friends HTML file within the data files folder
    close_friends_path = os.path.join(script_dir, config.data_dir, config.connections_dir, config.followers_dir, "close_friends.html")
    
    # Load the HTML content with error handling
    close_friends_html = load_html_content(close_friends_path)
    
    # Parse the HTML content using BeautifulSoup
    close_friends_soup = BeautifulSoup(close_friends_html, "html.parser")
    
    # Extract close friends usernames
    close_friends_usernames = extract_usernames(close_friends_soup)
    
    # Define output directory and create it if it does not exist
    output_dir = create_output_dir(script_dir)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "close_friends.txt")
    write_to_file_detailed(output_file_path, close_friends_usernames, "Number of close friends", "Users on close friends list")
    
    # Print out confirmation of file export
    print(f"Close friends list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
