# Import required libraries
import os
from bs4 import BeautifulSoup

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Load the HTML content of the followers and following files
with open("./connections/followers_and_following/followers_1.html", "r", encoding="utf-8") as file:
    followers_html = file.read()

with open("./connections/followers_and_following/following.html", "r", encoding="utf-8") as file:
    following_html = file.read()

# Parse the HTML content using BeautifulSoup
followers_soup = BeautifulSoup(followers_html, "html.parser")
following_soup = BeautifulSoup(following_html, "html.parser")

# Function to extract usernames from the provided HTML content
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Extract followers and following usernames
followers_usernames = extract_usernames(followers_soup)
following_usernames = extract_usernames(following_soup)

# Find account names the user is following, that are not following them back
not_following_back = following_usernames - followers_usernames

# Output the result
print(not_following_back)
