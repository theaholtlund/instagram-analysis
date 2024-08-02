# Import required libraries
import os
from bs4 import BeautifulSoup
from collections import Counter
import variables
from utils import load_html_content, write_to_file_simple, create_output_dir, get_script_dir

# Function to extract comments
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define the path for the comments folder
    comments_path = os.path.join(script_dir, variables.data_dir, variables.activity_dir, variables.comments_dir)
    
    # Initialise the comment list
    all_comments = []
    
    # Iterate over all files in the comments directory
    for filename in os.listdir(comments_path):
        file_path = os.path.join(comments_path, filename)
        
        # Load the HTML content
        comments_html = load_html_content(file_path)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = BeautifulSoup(comments_html, "html.parser")
        
        # Extract comments from the HTML content
        comments = extract_comments(comments_soup)
        
        # Add extracted comments to the list of all comments
        all_comments.extend(comments)
    
    # Count the frequency of each comment
    comment_counts = Counter(all_comments)
    
    # Filter out comments that were repeated more than once
    repeated_comments = {comment: count for comment, count in comment_counts.items() if count > 1}
    
    # Sort repeated comments by frequency in descending order and take the top 5
    top_repeated_comments = sorted(repeated_comments.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Define output directory and create it if it does not exist
    output_dir = create_output_dir(script_dir)
    
    # Prepare the output data
    if top_repeated_comments:
        output_data = ["Top 5 repeated comments and their counts:"]
        for comment, count in top_repeated_comments:
            formatted_comment = comment.replace("Comment", "").strip()
            output_data.append(f"- {formatted_comment}, {count}")
    else:
        output_data = ["no repeated comments"]

    # Output the result to a file
    output_file_path = os.path.join(output_dir, "content_comments.txt")
    write_to_file_simple(output_file_path, output_data, "Repeated comments status")
    
    # Print out confirmation of file export
    if top_repeated_comments:
        print(f"Top 5 repeated comments have been saved to '{output_file_path}'.")
    else:
        print(f"No repeated comments found. Status saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
