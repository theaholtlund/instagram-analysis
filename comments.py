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

# Function to extract comments from the provided HTML content
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

# Function to write results to a file
def write_to_file(file_path, count):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Total number of comments left on Instagram: {count}\n")

# Main function to orchestrate the process
def main():
    data_dir = "instagram_data"
    activity_dir = "your_instagram_activity"
    comments_dir = "comments"
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Define the path for the comments folder
    comments_path = os.path.join(script_dir, data_dir, activity_dir, comments_dir)
    
    # Initialise the comment count
    total_comments = 0
    
    # Iterate over all files in the comments directory
    for filename in os.listdir(comments_path):
        file_path = os.path.join(comments_path, filename)
        
        # Load the HTML content
        comments_html = load_html_content(file_path)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = BeautifulSoup(comments_html, "html.parser")
        
        # Extract comments from the HTML content
        comments = extract_comments(comments_soup)
        
        # Update the total comment count
        total_comments += len(comments)
    
    # Define output directory and create it if it does not exist
    output_dir = os.path.join(script_dir, "analysis_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "number_of_comments.txt")
    write_to_file(output_file_path, total_comments)
    
    # Print out confirmation of file export
    print(f"The total number of comments left by the user has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
