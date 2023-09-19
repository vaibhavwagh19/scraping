# Wikipedia Infobox and Paragraph Scraper

## Overview

This Python script, `wikibot.py`, is a web scraper designed to extract and display information from Wikipedia pages. It utilizes the `requests` library for making HTTP requests and `BeautifulSoup` for parsing HTML content. The primary purpose of this script is to scrape data from Wikipedia infoboxes and retrieve the first two paragraphs of text from a specified Wikipedia page.

## Features

- **Infobox Data Extraction**: The script can extract structured data from Wikipedia infoboxes, which often contain key details about the topic of the page.

- **Paragraph Retrieval**: It retrieves and displays the first two paragraphs of text from the Wikipedia page, providing an overview of the topic.

- **User Interaction**: The script prompts the user to input a search keyword, and it then generates a Wikipedia URL based on the keyword, making it easy to scrape information on various topics.

## Usage

1. **Installation**: Ensure you have Python installed on your system. You can also install the `requests` library using `pip install requests`.

2. **Running the Script**: Execute the script `wikibot.py`. It will prompt you to enter a search keyword.

3. **Keyword Formatting**: The script formats the keyword, capitalizing each word and joining them with underscores to create a Wikipedia-friendly URL.

4. **Data Extraction**: It then sends an HTTP request to the Wikipedia page, extracts information from the infobox (if available), and retrieves the first two paragraphs of text.

5. **Output**: The script displays the extracted data in a structured format, making it easy to read and understand.

## Example

Suppose you want to learn more about a specific topic on Wikipedia. You can run the script, enter your search keyword, and quickly retrieve relevant information, including infobox details and introductory paragraphs.

## Note

Please use this script responsibly and in compliance with Wikipedia's API usage policies. Be aware of rate limits and any terms of use specified by Wikipedia.
