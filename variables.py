# Define configuration variables for files
liked_posts_file = "liked_posts.html"
liked_comments_file = "liked_comments.html"

# Define configuration variables for folders
data_dir = "instagram_data"
likes_dir = "likes"
connections_dir = "connections"
followers_dir = "followers_and_following"
activity_dir = "your_instagram_activity"
comments_dir = "comments"
output_dir = "analysis_outputs"

# Define the HTML template for summary report
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analysis Summary Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1, h2 {{ color: #2c3e50; }}
        details {{ margin: 10px 0; }}
        summary {{ cursor: pointer; font-weight: bold; }}
        .content-list {{ padding-left: 20px; }}
    </style>
</head>
<body>
    <h1>Analysis Summary Report</h1>
    {content}
    <h2>End of summary report</h2>
</body>
</html>
"""
