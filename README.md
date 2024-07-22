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

Before running the various scripts, please copy all contents from the folder they are in upon download as they are, with its current structure, into the `instagram_data` folder within the project directory.

### Running the Analysis

To utilise the script:

1. Run the script for which you want to perform an analysis.
2. Once the analysis is complete, you will find the output in the `analysis_outputs` directory, with a name corresponding to the area of analysis.

### Repository Contents

The repository currently contains four main scripts:

- `blocked_accounts`: Counts the number of blocked accounts, and outputs their username.
- `close_friends`: Counts the number of close friends, and outputs their username.
- `count_comments`: Counts the total number of comments made on Instagram posts.
- `count_liked_posts`: Calculates the total number of Instagram posts liked by the user.
- `find_unfollowers`: Identifies users who have unfollowed the account being analysed.
- `most_liked_posts`: Finds and lists the top accounts to which the user has given the most likes.
