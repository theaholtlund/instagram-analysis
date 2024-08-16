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
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 20px; 
            background-color: #f0f2f5; 
            color: #333; 
            line-height: 1.6;
        }}
        h1, h2 {{ 
            color: #2c3e50; 
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        h2 {{ font-size: 1.5em; }}
        details {{ 
            margin: 10px 0; 
            border: 1px solid #ddd; 
            padding: 10px; 
            background-color: #fff;
            border-radius: 5px;
        }}
        summary {{ 
            cursor: pointer; 
            font-weight: bold; 
            padding: 5px;
            display: flex; 
            align-items: center;
        }}
        summary:hover {{
            background-color: #ecf0f1;
            border-radius: 5px;
        }}
        summary::marker {{
            content: "► ";
        }}
        details[open] summary::marker {{
            content: "▼ ";
        }}
        .content-list {{ 
            padding-left: 20px; 
            margin-top: 10px;
        }}
        .content-list p {{ 
            margin: 5px 0; 
            padding: 5px; 
            background-color: #e9f5ff; 
            border-left: 3px solid #3498db;
            border-radius: 3px;
        }}
        @media (max-width: 600px) {{
            body {{
                margin: 10px;
            }}
            h1, h2 {{
                font-size: 1.2em;
            }}
            .content-list p {{
                font-size: 0.9em;
            }}
        }}
    </style>
</head>
<body>
    <h1>Analysis Summary Report</h1>
    {content}
    <h2>End of summary report</h2>
</body>
</html>
"""

