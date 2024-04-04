# Instagram Followers App

### Overview

The script is intended to be added to the directory of files received from Instagram when requesting your data from them. It analyses the data to identify accounts that you are following but are not following you back. Results are saved to a file for easy access.

### Requesting Files

To request data from Instagram:

1. Go to "Settings" > "Accounts Centre" > "Download your information"
2. Choose profiles and data range
3. Specify that the date range should be "All time" and that the format should be "HTML"
4. Confirm choices by clicking "Create files"
5. Expect an email with the download link within 30 days

### Setting Up Your Instagram Data

Before running the script, ensure you have placed the files `followers_1.html` and `following.html` from the directory `connections` > `followers_and_following` in the data you received from Instagram, in the `instagram_data` folder within the project directory.

### Using the Script

To utilise the script:

1. Run `find_users.py`. The script will analyse the follower information files located in the `instagram_data` folder.
2. Once the analysis is complete, you will find the output in the same folder named `not_following_back.txt`.
3. Open the file to see what user accounts you are following, but that are not following you back.

### Error Handling

If the necessary HTML files are not found within the `instagram_data` folder, the script will terminate with an error message.
