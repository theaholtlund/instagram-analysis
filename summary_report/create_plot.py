# Import required libraries
import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Ensure project root is in the path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Import modules and variables
import variables
from utils import load_and_parse_html, extract_content, read_file

# Set path for shared output directory
output_dir = Path(variables.OUTPUT_DIR)
file_path_bar = output_dir / variables.PLOT_BAR_CHART
file_path_pie = output_dir / variables.PLOT_PIE_CHART
file_path_following = output_dir / variables.PLOT_FOLLOWING_CHART

def read_total_from_file(file_path, label):
    """Read total counts from a file."""
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Error: {label} file '{file_path}' not found.")
        return None

    try:
        content = read_file(file_path)
        return int(content.split(":")[1].strip())
    except (ValueError, IndexError) as e:
        print(f"Error reading {label} data in '{file_path}': {e}")
        return None

def create_activity_plots(comments_file, likes_file):
    """Generate and save charts showing total likes, comments and their ratio."""
    total_comments = read_total_from_file(comments_file, "comments")
    total_likes = read_total_from_file(likes_file, "likes")
    if total_comments is None or total_likes is None:
        return

    try:
        # Define design for bar chart
        plt.figure(figsize=(8, 5))
        plt.bar(["Likes", "Comments"], [total_likes, total_comments], 
                color=[variables.PLOT_COLOUR_LIGHT, variables.PLOT_COLOUR_DARK])
        plt.title("Total Instagram Activity: Likes and Comments")
        plt.xlabel("Activity Type")
        plt.ylabel("Count")
        plt.savefig(file_path_bar, dpi=150, bbox_inches="tight")
        plt.close()

        # Define design for pie chart
        plt.figure(figsize=(6, 6))
        plt.pie([total_likes, total_comments], labels=["Likes", "Comments"],
                autopct="%1.1f%%", startangle=140,
                colors=[variables.PLOT_COLOUR_LIGHT, variables.PLOT_COLOUR_DARK],
                wedgeprops={"edgecolor": "black", "linewidth": 1})
        plt.title("Likes-to-Comments Ratio")
        plt.savefig(file_path_pie, dpi=150, bbox_inches="tight")
        plt.close()

        print(f"Charts saved to: {output_dir}")
    except Exception as e:
        print(f"Error creating charts: {e}")

def create_close_friends_plot(close_friends_file, following_file):
    """Generate and save a plot showing the percentage ratio between following and close friends."""
    close_friends_file = Path(close_friends_file)
    following_file = Path(following_file)

    if not close_friends_file.exists():
        print(f"Error: Close friends file '{close_friends_file}' not found.")
        return

    try:
        # Get the number of close friends, in first line
        close_friends_data = close_friends_file.read_text(encoding="utf-8").strip()
        num_close_friends_line = next(line for line in close_friends_data.splitlines() if "Number of close friends:" in line)
        num_close_friends = int(num_close_friends_line.split(":")[1].strip())
    except (ValueError, IndexError, StopIteration) as e:
        print(f"Error parsing the number of close friends from '{close_friends_file}': {e}")
        return

    # Parse the following HTML content using BeautifulSoup
    following_soup = load_and_parse_html(following_file)
    if not following_soup:
        print(f"Error parsing the following HTML file '{following_file}'.")
        return
    
    # Extract usernames for following from the HTML content
    following_usernames = extract_content(following_soup, tag="a", content_type="text")

    # Calculate the percentage of close friends, avoid division by zero error
    total_following = len(following_usernames)
    percentage = (num_close_friends / total_following) * 100 if total_following > 0 else 0

    # Create the plot
    plt.figure(figsize=(8, 5))
    bars = plt.bar(["Close Friends", "Others"],
                   [num_close_friends, total_following - num_close_friends],
                   color=[variables.PLOT_COLOUR_LIGHT, variables.PLOT_COLOUR_DARK])
    plt.title(f"Following vs Close Friends\nClose Friends: {num_close_friends} | Following: {total_following}\nPercentage: {percentage:.2f}%")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.tight_layout()

    # Annotate bars with their value
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=10)

    # Save the plot
    plt.savefig(file_path_following, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Plot saved to: {output_dir}")
