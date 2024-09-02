# Instagram Analysis App

### Overview

The repository can be used to analyse various areas for Instagram, based on files received when a user requests their data from the platform. Files are names according to their functionality. Results are saved to a file for easy access.

### Requesting Data

To request data from Instagram:

1. Go to "Settings" > "Accounts Centre" > "Information and Permissions" > "Download Your Information".
2. Choose profiles and data range, by choosing to download all your data.
3. Specify that the date range should be "All time" and that the format should be "HTML".
4. Confirm choices by clicking "Create files".
5. Expect an e-mail with the download link within 30 days.

### Adding Data

Before running the analysis scripts, please copy all contents from the download folder as they are, with its current structure, into the `instagram_data` project folder.

### Running the Analysis

To utilise the script:

1. All analysis scripts are located in the `analysis_scripts` directory. Run the script for which you want to perform an analysis.
2. Once the analysis is complete, the output can be found in the `analysis_outputs` directory, with a name corresponding to the area of analysis.

### Repository Contents

#### Scripts for Analysis:

- `blocked_accounts`: Finds the number of blocked accounts, and their usernames.
- `close_friends`: Finds the number of close friends, and their usernames.
- `content_comments`: Finds the top most repeated comments made on Instagram posts.
- `count_comments`: Finds the total number of comments made on Instagram posts.
- `count_liked_comments`: Finds the total number of comments liked by the user.
- `count_liked_posts`: Finds the total number of Instagram posts liked by the user.
- `most_liked_posts`: Finds the accounts to which the user has given the most likes.
- `not_following_back`: Finds users who the account follows that does not follow back.

#### Scripts for Summary Report:

A summary report of all analysis outputs can be generated through the `generate_report` file, located in the `summary_report` directory, once all scripts have been executed. The report will be created in the same directory, and automatically open in a browser once generated.

#### Shared Functionality Files:

- `utils`: For functionality shared between scripts, such as writing to file.
- `variables`: Stores shared variables, such as file and directory names for analysis data.
