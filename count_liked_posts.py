# Import required libraries
import os
from bs4 import BeautifulSoup
import variables
from utils import load_html_content, write_to_file_simple, create_output_dir, get_script_dir

# Function to extract likes from the provided HTML content
def extract_likes(soup):
    return [like for like in soup.find_all("a", href=True) if like.text == "👍"]

# Main function to coordinate execution of the script
def main():
    # Get the directory of the current script
    script_dir = get_script_dir()
    
    # Define the path for the likes folder
    likes_path = os.path.join(script_dir, variables.data_dir, variables.activity_dir, variables.likes_dir)
    
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
    output_dir = create_output_dir(script_dir)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "count_liked_posts.txt")
    write_to_file_simple(output_file_path, [total_likes], "Total number of likes given on Instagram")
    
    # Print out confirmation of file export
    print(f"The total number of likes given by the user has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
