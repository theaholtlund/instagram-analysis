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

# Function to count the number of blocked accounts from the provided HTML content
def count_blocked_accounts(soup):
    return len(soup.find_all("a", href=True))

# Function to write results to a file
def write_to_file(file_path, count):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Number of blocked accounts: {count}\n")

# Main function to coordinate execution of the script
def main():
    data_dir = "instagram_data"
    connections_dir = "connections"
    followers_dir = "followers_and_following"
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Define path for the blocked accounts HTML file within the data files folder
    blocked_accounts_path = os.path.join(script_dir, data_dir, connections_dir, followers_dir, "blocked_accounts.html")
    
    # Load the HTML content with error handling
    blocked_accounts_html = load_html_content(blocked_accounts_path)
    
    # Parse the HTML content using BeautifulSoup
    blocked_accounts_soup = BeautifulSoup(blocked_accounts_html, "html.parser")
    
    # Count blocked accounts
    blocked_accounts_count = count_blocked_accounts(blocked_accounts_soup)
    
    # Define output directory and create it if it does not exist
    output_dir = os.path.join(script_dir, "analysis_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "blocked_accounts.txt")
    write_to_file(output_file_path, blocked_accounts_count)
    
    # Print out confirmation of file export
    print(f"Blocked accounts count has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
