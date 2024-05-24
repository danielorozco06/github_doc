"""
File to download a GitHub documentation page and convert it to a PDF file.
"""

import os
import re

import pdfkit  # type: ignore
import requests
from bs4 import BeautifulSoup

# Step 1: Download the webpage
url = "https://docs.github.com/es/code-security/codeql-cli/getting-started-with-the-codeql-cli/about-the-codeql-cli"
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

# Extract the title for the PDF filename
title_element = soup.find(id="title-h1")
if title_element is not None:
    title = title_element.text
else:
    title = ""

# Remove any non-alphanumeric characters
if title is not None:
    title = re.sub(r"\W+", "", title)
else:
    title = ""

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

# Define the output path
file = os.path.join("output", f"{title}.pdf")

pdfkit.from_string(clean_html, file, options=options)
