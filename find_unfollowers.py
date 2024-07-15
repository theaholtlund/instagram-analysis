# Import required libraries
import os
from bs4 import BeautifulSoup

# Function to load HTML content with error handling
def load_html_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: '{file_path}' not found. Please make sure you have copied the files into the 'instagram_data' folder.")

# Function to extract usernames from the provided HTML content
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Function to write results to a file
def write_to_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Accounts not following back:\n")
        for username in data:
            file.write(f"- {username}\n")

# Main function to orchestrate the process
def main():
    # Specify the directory where Instagram data is expected to be placed
    data_dir = "instagram_data"
    connections_dir = "connections"
    followers_dir = "followers_and_following"
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Define paths for the HTML files within the data files folder
    followers_path = os.path.join(script_dir, data_dir, connections_dir, followers_dir, "followers_1.html")
    following_path = os.path.join(script_dir, data_dir, connections_dir, followers_dir, "following.html")
    
    try:
        # Load the HTML content with error handling
        followers_html = load_html_content(followers_path)
        following_html = load_html_content(following_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    # Parse the HTML content using BeautifulSoup
    followers_soup = BeautifulSoup(followers_html, "html.parser")
    following_soup = BeautifulSoup(following_html, "html.parser")
    
    # Extract followers and following usernames
    followers_usernames = extract_usernames(followers_soup)
    following_usernames = extract_usernames(following_soup)
    
    # Find account names the user is following, that are not following them back
    not_following_back = following_usernames - followers_usernames
    
    # Define output directory and create it if it does not exist
    output_dir = os.path.join(script_dir, "analysis_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "not_following_back.txt")
    write_to_file(output_file_path, not_following_back)
    
    # Print out confirmation of file export
    print(f"Accounts not following back have been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
