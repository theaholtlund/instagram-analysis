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

# Function to extract likes from the provided HTML content
def extract_likes(soup):
    return [like for like in soup.find_all("a", href=True) if like.text == "👍"]

# Function to write results to a file
def write_to_file(file_path, count):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Total number of likes given on Instagram: {count}\n")

# Main function to orchestrate the process
def main():
    data_dir = "instagram_data"
    activity_dir = "your_instagram_activity"
    likes_dir = "likes"
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Define the path for the likes folder
    likes_path = os.path.join(script_dir, data_dir, activity_dir, likes_dir)
    
    # Initialise the likes count
    total_likes = 0
    
    # Iterate over all files in the likes directory
    for filename in os.listdir(likes_path):
        file_path = os.path.join(likes_path, filename)
        
        # Load the HTML content
        likes_html = load_html_content(file_path)
        
        # Parse the HTML content using BeautifulSoup
        likes_soup = BeautifulSoup(likes_html, "html.parser")
        
        # Extract likes from the HTML content
        likes = extract_likes(likes_soup)
        
        # Update the total likes count
        total_likes += len(likes)
    
    # Define output directory and create it if it does not exist
    output_dir = os.path.join(script_dir, "analysis_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "count_liked_posts.txt")
    write_to_file(output_file_path, total_likes)
    
    # Print out confirmation of file export
    print(f"The total number of likes given by the user has been saved to '{output_file_path}'.")
