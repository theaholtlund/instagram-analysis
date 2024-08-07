# Import required libraries
import os
import variables
from utils import get_script_dir, read_file, load_and_parse_html, write_to_file_detailed

# Function to extract usernames
def extract_usernames(soup):
    return {a['href'].split("/_u/")[-1] for a in soup.find_all("a", href=True)}

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define path for the blocked accounts HTML file
    blocked_accounts_path = os.path.join(script_dir, variables.data_dir, variables.connections_dir, variables.followers_dir, "blocked_accounts.html")
    
    # Load and parse the HTML content
    blocked_accounts_soup = load_and_parse_html(blocked_accounts_path)
    
    # Extract blocked accounts usernames
    blocked_accounts_usernames = extract_usernames(blocked_accounts_soup)
    
    # Output the result to a file
    output_file_path = os.path.join(variables.output_dir, "blocked_accounts.txt")
    write_to_file_detailed(output_file_path, blocked_accounts_usernames, "Number of blocked accounts", "Blocked accounts")
    
    # Print out confirmation of file export
    print(f"Blocked accounts list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
