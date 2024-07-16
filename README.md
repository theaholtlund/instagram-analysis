# Instagram Analysis App

### Overview

The repository can be used to analyse various areas for Instagram, based on files received when a user requests their data from the platform. Files are names according to their functionality. Results are saved to a file for easy access.

### Requesting Files

To request data from Instagram:

1. Go to "Settings" > "Accounts Centre" > "Download your information"
2. Choose profiles and data range
3. Specify that the date range should be "All time" and that the format should be "HTML"
4. Confirm choices by clicking "Create files"
5. Expect an e-mail with the download link within 30 days

### Setting Up Your Instagram Data

Before running the respective scripts, please copy all contents from the downloaded folder as they are, with the current structure, into the `instagram_data` folder within the project directory.

### Using the Script

To utilise the script:

1. Run the script for which you want to perform an analysis.
2. Once the analysis is complete, you will find the output in the `analysis_outputs` directory, with a name corresponding to the area of analysis.

### Error Handling

If the necessary HTML files are not found within the `instagram_data` folder, the script will terminate with an error message.
