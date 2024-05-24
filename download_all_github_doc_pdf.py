"""
File to download multiple GitHub documentation pages and convert them to a single PDF file.
"""

import os

import pdfkit  # type: ignore
import requests
from bs4 import BeautifulSoup

# Open the file with the URLs
with open("output/links.txt", "r") as f:
    urls = f.readlines()

# Get the first URL and extract the antepenultimate and penultimate parts
first_url = urls[0].strip()
parts = first_url.split("/")
pdf_name = parts[-3] + "_" + parts[-2] + ".pdf"

# Define the output path
file = os.path.join("output", pdf_name)

# Initialize an empty string to hold all HTML content
all_html = ""

# Loop over each URL
for url in urls:
    url = url.strip()

    # Step 1: Download the webpage
    response = requests.get(url)
    html = response.text

    # Step 2: Extract the main content
    soup = BeautifulSoup(html, "html.parser")

    # Remove elements with data-container="toc"
    for element in soup.find_all(attrs={"data-container": "toc"}):
        element.decompose()

    # Includes only the div with id="main-content"
    main_content = soup.find(id="main-content")
    clean_html = str(main_content)

    # Add the clean HTML to the all_html string
    all_html += clean_html

# Step 3: Convert to PDF
options = {
    "quiet": "",
    "encoding": "UTF-8",
    "no-images": False,
    "custom-header": [
        (
            "User-Agent",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        )
    ],
}

pdfkit.from_string(all_html, file, options=options)
