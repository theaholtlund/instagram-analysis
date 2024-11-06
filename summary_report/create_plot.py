# Import required libraries
from pathlib import Path
import matplotlib.pyplot as plt

def create_activity_plot(output_path, comments_file, likes_file):
    """Generate and save charts showing total likes, comments and their ratio."""
    comments_path = Path(comments_file)
    likes_path = Path(likes_file)

    try:
        with comments_path.open("r") as f:
            comments_line = f.readline().strip()
            total_comments = int(comments_line.split(":")[1].strip())
        
        with likes_path.open("r") as f:
            likes_line = f.readline().strip()
            total_likes = int(likes_line.split(":")[1].strip())
    except (FileNotFoundError, ValueError, IndexError) as e:
        print("Error reading data files:", e)
        return

    # Create a bar chart for total likes and comments
    bar_chart_path = output_path.parent / "activity_chart_bar.png"
    plt.figure(figsize=(8, 5))
    plt.bar(["Likes", "Comments"], [total_likes, total_comments], color=["orange", "red"])
    plt.title("Total Instagram Activity: Likes and Comments")
    plt.ylabel("Count")

    print(f"Bar chart saved to: {bar_chart_path}")
