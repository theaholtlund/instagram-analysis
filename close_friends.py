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

# Function to extract usernames from the provided HTML content
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Function to write results to a file
def write_to_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Total close friends: {len(data)}\n")
        file.write("Close Friends:\n")
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
    
    # Define path for the close friends HTML file within the data files folder
    close_friends_path = os.path.join(script_dir, data_dir, connections_dir, followers_dir, "close_friends.html")
    
    # Load the HTML content with error handling
    close_friends_html = load_html_content(close_friends_path)
    
    # Parse the HTML content using BeautifulSoup
    close_friends_soup = BeautifulSoup(close_friends_html, "html.parser")
    
    # Extract close friends usernames
    close_friends_usernames = extract_usernames(close_friends_soup)
    
    # Define output directory and create it if it does not exist
    output_dir = os.path.join(script_dir, "analysis_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "close_friends_list.txt")
    write_to_file(output_file_path, close_friends_usernames)
    
    # Print out confirmation of file export
    print(f"Close friends list has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
