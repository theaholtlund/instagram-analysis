# Import required libraries
import os
import sys
from collections import Counter

# Add project root directory to system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import the required modules
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file

# Function to extract usernames behind liked posts
def extract_liked_usernames(soup):
    return [username.text for username in soup.find_all("div", class_="_3-95 _2pim _a6-h _a6-i")]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Load, parse and extract liked posts from HTML content
    likes_path = construct_file_path(script_dir, variables.data_dir, variables.activity_dir, variables.likes_dir, "liked_posts.html")
    likes_soup = load_and_parse_html(likes_path)
    liked_usernames = extract_liked_usernames(likes_soup)
    
    # Count occurrences of each username
    username_counts = Counter(liked_usernames)
    
    # Get the top 5 usernames with the most likes
    top_5_liked_users = username_counts.most_common(5)
    
    # Prepare output data with proper formatting
    header = "Top 5 users who you liked the most posts from:"
    output_data = [f"- {username}: {count}" for username, count in top_5_liked_users]
    formatted_header = f"{header}\n"
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.output_dir, "most_liked_posts.txt")
    write_to_file(output_file_path, data=output_data, header=formatted_header, detailed=False)
    print(f"Top users received the most likes on their posts have been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
