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
    """Extract close friends from HTML and save to text file."""
    script_dir = get_script_dir()
    
    # Load, parse and extract close friends accounts from HTML content
    close_friends_path = construct_file_path(script_dir, variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR, variables.CLOSE_FRIENDS_FILE)
    close_friends_soup = load_and_parse_html(close_friends_path)

    # Extract URLs and then convert to usernames
    close_friends_usernames = extract_content(close_friends_soup, tag="a", content_type="href")

    # Extract only the username from each URL
    usernames_only = {url.split('/')[-1] for url in close_friends_usernames}

    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "close_friends.txt")
    write_to_file(output_file_path, usernames_only, "Number of close friends", detailed=True, data_label="Users on close friends list")
    print(f"Close friends list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
