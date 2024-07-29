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

Before running the analysis scripts, please copy all contents from the download folder as they are, with its current structure, into the `instagram_data` folder within the project directory.

### Running the Analysis

To utilise the script:

1. Run the script for which you want to perform an analysis.
2. Once the analysis is complete, the output can be found in the `analysis_outputs` directory, with a name corresponding to the area of analysis.

### Repository Contents

Supporting files:

- `utils`: For functionality shared between scripts, such as writing to file
- `variables`: Stores set variables, such as directory names for analysis data

The repository currently contains the following analysis scripts:

- `blocked_accounts`: Finds the number of blocked accounts, and their usernames.
- `close_friends`: Finds the number of close friends, and their usernames.
- `count_comments`: Finds the total number of comments made on Instagram posts.
- `count_liked_posts`: Finds the total number of Instagram posts liked by the user.
- `most_liked_posts`: Finds the accounts to which the user has given the most likes.
- `not_following_back`: Finds users who the account being analysed follows but they do not follow the account back.

Furthermore, a summary report of all the outputs can be generated through the `summary_report` file, once each analysis script has been executed, for a combined output file.
