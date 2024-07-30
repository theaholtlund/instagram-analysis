# Import required libraries
import os
from bs4 import BeautifulSoup
from collections import Counter
import variables
from utils import load_html_content, write_to_file_simple, create_output_dir, get_script_dir

# Function to extract usernames behind liked post
def extract_liked_usernames(soup):
    return [username.text for username in soup.find_all("div", class_="_3-95 _2pim _a6-h _a6-i")]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define paths for the HTML files within the data files folder
    likes_path = os.path.join(script_dir, variables.data_dir, variables.activity_dir, variables.likes_dir, "liked_posts.html")
    
    # Load the HTML content
    likes_html = load_html_content(likes_path)
    
    # Parse the HTML content using BeautifulSoup
    likes_soup = BeautifulSoup(likes_html, "html.parser")
    
    # Extract liked post usernames
    liked_usernames = extract_liked_usernames(likes_soup)
    
    # Count occurrences of each username
    username_counts = Counter(liked_usernames)
    
    # Get the top 5 usernames with the most likes
    top_5_liked_users = username_counts.most_common(5)
    
    # Define output directory and create it if it does not exist
    output_dir = create_output_dir(script_dir)
    
    # Format the data for output
    formatted_data = [f"\n- {username}: {count}" for username, count in top_5_liked_users]
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "most_liked_posts.txt")
    write_to_file_simple(output_file_path, formatted_data, "Top 5 users who you liked the most posts from")
    
    # Print out confirmation of file export
    print(f"The top 5 users who you liked the most posts from have been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
