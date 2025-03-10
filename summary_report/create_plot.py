# Import required libraries
import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Ensure project root is in the path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Import modules and variables
import variables
from utils import load_and_parse_html, read_file, extract_content

# Define shared paths for plots
output_dir = Path(variables.OUTPUT_DIR)

def read_total_from_file(file_path, label):
    """Read total counts from a file."""
    try:
        content = read_file(file_path)
        return int(content.split(":")[1].strip())
    except (ValueError, IndexError, AttributeError):
        print(f"Error reading {label} data in '{file_path}'.")
        return None

def save_plot(fig, file_path):
    """Save the given plot to a file."""
    fig.savefig(file_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

def create_activity_plots(comments_file, likes_file):
    """Generate and save charts showing total likes, comments and their ratio."""
    total_comments = read_total_from_file(comments_file, "comments")
    total_likes = read_total_from_file(likes_file, "likes")

    if None in [total_comments, total_likes]:
        return

    # Create bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(["Likes", "Comments"], [total_likes, total_comments], 
           color=[variables.PLOT_COLOUR_LIGHT, variables.PLOT_COLOUR_DARK])
    ax.set_title("Total Instagram Activity: Likes and Comments")
    ax.set_xlabel("Activity Type")
    ax.set_ylabel("Count")
    save_plot(fig, output_dir / variables.PLOT_BAR_CHART)

    # Create pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie([total_likes, total_comments], labels=["Likes", "Comments"], autopct="%1.1f%%", 
           startangle=140, colors=[variables.PLOT_COLOUR_LIGHT, variables.PLOT_COLOUR_DARK],
           wedgeprops={"edgecolor": "black", "linewidth": 1})
    ax.set_title("Likes-to-Comments Ratio")
    save_plot(fig, output_dir / variables.PLOT_PIE_CHART)

    print(f"Charts saved to {output_dir}")

def create_close_friends_plot(close_friends_file, following_file):
    """Generate a plot showing the percentage of close friends among those followed."""
    try:
        # Get number of close friends, located in first line
        close_friends_data = read_file(close_friends_file, as_lines=True)
        num_close_friends = int(next(line for line in close_friends_data if "Number of close friends:" in line).split(":")[1].strip())
    except (ValueError, IndexError, StopIteration, AttributeError):
        print(f"Error parsing the number of close friends from '{close_friends_file}'.")
        return

    # Parse following HTML content using BeautifulSoup
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
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(["Close Friends", "Others"], 
                  [num_close_friends, total_following - num_close_friends],
                  color=[variables.PLOT_COLOUR_LIGHT, variables.PLOT_COLOUR_DARK])
    ax.set_title(f"Following vs Close Friends\nClose Friends: {num_close_friends} | Following: {total_following}\nPercentage: {percentage:.2f}%")
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")
    ax.bar_label(bars, fmt="%.0f", padding=3)
    save_plot(fig, output_dir / variables.PLOT_FOLLOWING_CHART)

    print(f"Plot saved to {output_dir}")
