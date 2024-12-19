# Import required libraries
import sys
from pathlib import Path

# Ensure project root is in the path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file, extract_content

def main():
    """Extract blocked accounts from HTML and save to text file."""
    script_dir = get_script_dir()

    # Load, parse and extract blocked accounts from HTML content
    blocked_accounts_path = construct_file_path(script_dir, variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR, variables.BLOCKED_PROFILES_FILE)
    blocked_accounts_soup = load_and_parse_html(blocked_accounts_path)
    blocked_accounts_usernames = extract_content(blocked_accounts_soup, tag="a", attr={"href": True}, content_type="href")

    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "blocked_accounts.txt")
    write_to_file(output_file_path, blocked_accounts_usernames, "Number of blocked accounts", detailed=True, data_label="Blocked accounts")
    print(f"Blocked accounts list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
