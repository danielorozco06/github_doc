"""
File to extract all links from the GitHub Copilot documentation page
"""

import subprocess

import requests
from bs4 import BeautifulSoup

# Step 1: Download the webpage
url = "https://docs.github.com/es/copilot#all-docs"
response = requests.get(url)
html = response.text

# Step 2: Extract the main content
soup = BeautifulSoup(html, "html.parser")

# Get the element with class "d-flex gutter flex-wrap"
all_docs = soup.find(class_="d-flex gutter flex-wrap")

# Remove all elements with class "mb-3 f4"
for element in all_docs.find_all(class_="mb-3 f4"):  # type: ignore
    element.decompose()

# Check if all_docs is not None before calling find_all
if all_docs is not None:
    # Get all links in the webpage
    links = all_docs.find_all("a")  # type: ignore
else:
    links = []

# Extract href attribute from each link and filter out any None values
links = [link.get("href") for link in links if link.get("href") is not None]

# Write links to a text file with the prefix added
with open("output/links.txt", "w") as f:
    for link in links:
        f.write("https://docs.github.com/%s\n" % link)

# Execute the script
subprocess.run(["python", "download_all_github_doc_pdf.py"], check=True)
