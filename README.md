# Instagram Analysis App

### Overview

The repository can be used to analyse various areas for Instagram, based on files received when a user requests their data from the platform. Files are names according to their functionality. Currently, it only has functionality to find accounts that have unfollowed a user within the last year, but more functionality is under development. Results are saved to a file for easy access.

### Requesting Files

To request data from Instagram:

1. Go to "Settings" > "Accounts Centre" > "Download your information"
2. Choose profiles and data range
3. Specify that the date range should be "All time" and that the format should be "HTML"
4. Confirm choices by clicking "Create files"
5. Expect an email with the download link within 30 days

### Setting Up Your Instagram Data

Before running the respective scripts, please copy app contents from the downloaded folder into the
have placed the files `followers_1.html` and `following.html` from the directory `connections` > `followers_and_following` in the data you received from Instagram, in the `instagram_data` folder within the project directory.

### Using the Script

To utilise the script:

1. Run `find_unfollowers.py`. The script will analyse the follower information files located in the `instagram_data` folder.
2. Once the analysis is complete, you will find the output in the project directory, in a file called `not_following_back.txt`.
3. Open the file to see what user accounts you are following, but that are not following you back.

### Error Handling

If the necessary HTML files are not found within the `instagram_data` folder, the script will terminate with an error message.
