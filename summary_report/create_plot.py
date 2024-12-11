# Import required libraries
import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Add project root directory to system path if not already present
script_dir = Path(__file__).resolve().parent
root_dir = script_dir.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

# Import modules and variables
import variables
from utils import load_and_parse_html, extract_content

def read_total_from_file(file_path, label):
    """Helper function to read total counts from a file."""
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Error: {label} file '{file_path}' not found.")
        return None

    try:
        with file_path.open("r") as f:
            return int(f.readline().strip().split(":")[1].strip())
    except (ValueError, IndexError) as e:
        print(f"Error reading {label} data in '{file_path}': {e}")
        return None

def create_activity_plots(output_path, comments_file, likes_file):
    """Generate and save charts showing total likes, comments and their ratio."""
    total_comments = read_total_from_file(comments_file, "comments")
    total_likes = read_total_from_file(likes_file, "likes")
    
    if total_comments is None or total_likes is None:
        return

    output_dir = output_path.parent
    bar_chart_path = output_dir / "activity_chart_bar.png"
    pie_chart_path = output_dir / "activity_chart_pie.png"

    try:
        # Define design for bar chart
        plt.figure(figsize=(8, 5))
        plt.bar(["Likes", "Comments"], [total_likes, total_comments], color=[variables.COLOR_LIKES, variables.COLOR_COMMENTS])
        plt.title("Total Instagram Activity: Likes and Comments")
        plt.xlabel("Activity Type")
        plt.ylabel("Count")
        plt.savefig(bar_chart_path, dpi=150, bbox_inches="tight")
        plt.close()

        # Define design for pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(
            [total_likes, total_comments], labels=["Likes", "Comments"],
            autopct="%1.1f%%", startangle=140,
            colors=[variables.COLOR_LIKES, variables.COLOR_COMMENTS], wedgeprops={"edgecolor": "black", "linewidth": 1}
        )
        plt.title("Likes-to-Comments Ratio")
        plt.savefig(pie_chart_path, dpi=150, bbox_inches="tight")
        plt.close()

        print(f"Bar chart saved to: {bar_chart_path}")
        print(f"Pie chart saved to: {pie_chart_path}")
    except Exception as e:
        print(f"Error creating charts: {e}")

def create_close_friends_ratio_plot(output_path, close_friends_file, following_file, fig_size=(8, 5)):
    """Generate and save a plot showing the percentage ratio between following and close friends."""
    close_friends_file = Path(close_friends_file)
    following_file = Path(following_file)
    
    # Read the close friends file
    if not close_friends_file.exists():
        print(f"Error: Close friends file '{close_friends_file}' not found.")
        return
    
    with close_friends_file.open("r") as f:
        lines = f.readlines()
        
        # Get the number of close friends, in first line
        try:
            num_close_friends = int(lines[0].strip().split(":")[1].strip())
        except (ValueError, IndexError) as e:
            print(f"Error parsing the number of close friends from '{close_friends_file}': {e}")
            return
    
    # Read the following file (following.html)
    if not following_file.exists():
        print(f"Error: Following file '{following_file}' not found.")
        return
    
    # Parse the following HTML content using BeautifulSoup
    following_soup = load_and_parse_html(following_file)
    
    if following_soup is None:
        print(f"Error loading or parsing the following HTML file '{following_file}'.")
        return
    
    # Extract following usernames from the HTML content
    following_usernames = extract_content(following_soup, tag="a", content_type="text")
    
    # Calculate the percentage of close friends, avoid division by zero error
    if len(following_usernames) > 0:
        percentage = (num_close_friends / len(following_usernames)) * 100
    else:
        percentage = 0
    
    # Create the plot
    plt.figure(figsize=fig_size)
    bars = plt.bar(
        ["Close Friends in Following", "Others"], 
        [num_close_friends, len(following_usernames) - num_close_friends], 
        color=['green', 'gray']
    )
    plt.title(f"Following vs Close Friends\nClose Friends: {num_close_friends} | Following: {len(following_usernames)}\nPercentage: {percentage:.2f}%")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.tight_layout()

    # Add the numbers on top of the bars for verification
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2, height + 0.5,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=10
        )
    
    # Save the plot
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    
    print(f"Following vs Close Friends plot saved to: {output_path}")
