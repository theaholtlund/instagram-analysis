# Import required libraries
import os
from bs4 import BeautifulSoup
from utils import load_html_content, write_to_file_detailed

# Function to extract usernames from the provided HTML content
def extract_usernames(soup):
    return {a['href'].split("/_u/")[-1] for a in soup.find_all("a", href=True)}

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
    
    # Extract blocked accounts usernames
    blocked_accounts_usernames = extract_usernames(blocked_accounts_soup)
    
    # Define output directory and create it if it does not exist
    output_dir = os.path.join(script_dir, "analysis_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "blocked_accounts.txt")
    write_to_file_detailed(output_file_path, blocked_accounts_usernames, "Number of blocked accounts", "Blocked accounts")
    
    # Print out confirmation of file export
    print(f"Blocked accounts list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()