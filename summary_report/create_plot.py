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

def create_activity_plot(output_path, comments_file, likes_file, fig_size_bar=(8, 5), fig_size_pie=(6, 6)):
    """Generate and save charts showing total likes, comments and their ratio."""
    total_comments = read_total_from_file(comments_file, "comments")
    total_likes = read_total_from_file(likes_file, "likes")
    
    if total_comments is None or total_likes is None:
        return

    output_dir = output_path.parent
    bar_chart_path = output_dir / "activity_chart_bar.png"
    pie_chart_path = output_dir / "activity_chart_pie.png"

    try:
        # Bar chart
        plt.figure(figsize=fig_size_bar)
        plt.bar(["Likes", "Comments"], [total_likes, total_comments], color=[variables.COLOR_LIKES, variables.COLOR_COMMENTS])
        plt.title("Total Instagram Activity: Likes and Comments")
        plt.xlabel("Activity Type")
        plt.ylabel("Count")
        plt.savefig(bar_chart_path, dpi=150, bbox_inches="tight")
        plt.close()

        # Pie chart
        plt.figure(figsize=fig_size_pie)
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

def create_follower_growth_plot(growth_file):
    """Generate and save a line chart showing follower growth over time."""
    growth_file = Path(growth_file)
    if not growth_file.exists():
        print(f"Error: Growth file '{growth_file}' not found.")
        return

    try:
        # Line chart for growth
        plt.title("Instagram Follower Growth Over Time")

    except Exception as e:
        print(f"Error creating growth chart: {e}")
