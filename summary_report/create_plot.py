# Import required libraries
import matplotlib.pyplot as plt
from pathlib import Path

def create_activity_plot(comments_file, likes_file):
    comments_path = Path(comments_file)
    likes_path = Path(likes_file)

    try:
        with comments_path.open("r") as f:
            comments_line = f.readline().strip()
            total_comments = int(comments_line.split(":")[1].strip())
        
        with likes_path.open("r") as f:
            likes_line = f.readline().strip()
            total_likes = int(likes_line.split(":")[1].strip())
    except:
        print("Error reading data files")
