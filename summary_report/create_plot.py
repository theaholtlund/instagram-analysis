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