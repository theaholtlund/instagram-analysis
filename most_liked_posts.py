# Import required libraries
import os
from collections import Counter
import variables
from utils import get_script_dir, read_file, load_and_parse_html, write_to_file_simple

# Function to extract usernames behind liked post
def extract_liked_usernames(soup):
    return [username.text for username in soup.find_all("div", class_="_3-95 _2pim _a6-h _a6-i")]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define path for the likes HTML file
    likes_path = os.path.join(script_dir, variables.data_dir, variables.activity_dir, variables.likes_dir, "liked_posts.html")
    
    # Parse the HTML content using BeautifulSoup
    likes_soup = load_and_parse_html(likes_path)
    
    # Extract liked post usernames
    liked_usernames = extract_liked_usernames(likes_soup)
    
    # Count occurrences of each username
    username_counts = Counter(liked_usernames)
    
    # Get the top 5 usernames with the most likes
    top_5_liked_users = username_counts.most_common(5)
    
    # Format the data for output
    formatted_data = [f"\n- {username}: {count}" for username, count in top_5_liked_users]
    
    # Output the result to a file
    output_file_path = os.path.join(variables.output_dir, "most_liked_posts.txt")
    write_to_file_simple(output_file_path, formatted_data, "Top 5 users who you liked the most posts from")
    
    # Print out confirmation of file export
    print(f"The top 5 users who you liked the most posts from have been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
