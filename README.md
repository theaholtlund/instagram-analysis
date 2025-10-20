# Instagram Analysis App

## Overview

This project contains scripts to analyse various metrics from Instagram, based on files received when a user requests their data from the platform. Files are named according to functionality, and results are saved to a report for easy access.

## Requesting Data

To request data from Instagram:

1. Go to "Settings" > "Accounts Centre" > "Your Information and Permissions" > "Download Your Information".
2. Select your profile and then choose to download "All Available Information", then "Download to Device".
3. Specify that the date range should be "All Time" and that the format should be "HTML".
4. Confirm choices by clicking "Create Files".
5. Expect an e-mail with the download link within 30 days.

## Adding Data

Before running the analysis scripts, please copy all contents from the download folder as they are, with its current structure, into the `instagram_data` project folder.

## Create a Virtual Environment

Set up a virtual environment if desired (optional but recommended).

Windows:

```bash
python -m venv venv
.\venv\Scripts\Activate
```

MacOS and Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

Install `weasyprint`

```bash
brew install weasyprint
```

### Running the Analysis

To utilise the script:

- Run the `run_all_scripts.py` file to execute all analysis scripts in one batch, generating the required outputs.

```bash
python run_all_scripts.py
```

- Run the `generate_report.py` script. The report will be created in the same directory, and automatically open in the browser.

```bash
python summary_report/generate_report.py
```

### Repository Contents

#### Scripts for Analysis

- `blocked_accounts`: Finds the number of blocked accounts, and their usernames.
- `close_friends`: Finds the number of close friends, and their usernames.
- `content_comments`: Finds the top most repeated comments made on Instagram posts.
- `count_comments`: Finds the total number of comments made on Instagram posts.
- `count_liked_comments`: Finds the total number of comments liked by the user.
- `count_liked_posts`: Finds the total number of Instagram posts liked by the user.
- `count_stories`: Finds the total number of Instagram stories posted by the user.
- `most_liked_posts`: Finds the accounts to which the user has given the most likes.
- `not_following_back`: Finds users who the account follows that does not follow back.
