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

def create_activity_plot(output_path, comments_file, likes_file):
    """Generate and save charts showing total likes, comments and their ratio."""
    total_comments = read_total_from_file(comments_file, "comments")
    total_likes = read_total_from_file(likes_file, "likes")
    
    if total_comments is None or total_likes is None:
        return

    output_dir = output_path.parent

    try:
        # Bar chart for total likes and comments
        bar_chart_path = output_dir / "activity_chart_bar.png"
        plt.figure(figsize=(8, 5))
        plt.bar(["Likes", "Comments"], [total_likes, total_comments], color=[variables.COLOR_LIKES, variables.COLOR_COMMENTS])
        plt.title("Total Instagram Activity: Likes and Comments")
        plt.xlabel("Activity Type")
        plt.ylabel("Count")
        plt.savefig(bar_chart_path, dpi=150, bbox_inches="tight")
        plt.close()

        # Pie chart for likes-to-comments ratio
        pie_chart_path = output_dir / "activity_chart_pie.png"
        plt.figure(figsize=(6, 6))
        plt.pie(
            [total_likes, total_comments], labels=["Likes", "Comments"],
            autopct="%1.1f%%", startangle=140,
            colors=[variables.COLOR_LIKES, variables.COLOR_COMMENTS], wedgeprops={"edgecolor": "black", "linewidth": 1}
        )
        plt.title("Likes-to-Comments Ratio")
        plt.savefig(pie_chart_path, dpi=150, bbox_inches="tight")
        plt.close()

    except:
        print(f"Bar chart saved to: {bar_chart_path}")
        print(f"Pie chart saved to: {pie_chart_path}")
