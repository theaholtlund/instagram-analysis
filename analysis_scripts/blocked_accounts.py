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
    return {a['href'].split("/_u/")[-1] for a in soup.find_all("a", href=True)}

def main():
    # Get the current script directory
    script_dir = get_script_dir()

    # Load, parse and extract blocked accounts from HTML content
    blocked_accounts_path = construct_file_path(script_dir, variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR, variables.BLOCKED_PROFILES_FILE)
    blocked_accounts_soup = load_and_parse_html(blocked_accounts_path)
    blocked_accounts_usernames = extract_usernames(blocked_accounts_soup)

    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "blocked_accounts.txt")
    write_to_file(output_file_path, blocked_accounts_usernames, "Number of blocked accounts", detailed=True, data_label="Blocked accounts")
    print(f"Blocked accounts list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
