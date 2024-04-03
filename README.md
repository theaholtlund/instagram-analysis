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

### Using the Script

To utilise the script:

1. Request your information from Instagram, as described above
2. Once this is received, download it and place `find_users.py` in the directory
3. Execute the script to analyse the files containing follower information

### Error Handling

If the necessary HTML files are not found, the script will terminate with an error message, guiding the user to ensure that `find_users.py` is placed in the correct directory.
