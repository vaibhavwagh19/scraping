# Scraping
# Wikipedia Recent Articles Scraper

## Description

This Python script serves as a web scraper that utilizes the Wikipedia API to retrieve and display the titles of the 10 most recent articles on English Wikipedia. It leverages the `requests` library to make an HTTP GET request to the Wikipedia API, specifying parameters to fetch the desired data.

## How It Works

- The script defines the Wikipedia API endpoint and sets parameters, including the action, format, and the number of recent changes to retrieve.
- It sends an HTTP GET request to the Wikipedia API using the `requests.get()` method.
- If the request is successful (HTTP status code 200), it parses the JSON response and extracts the titles of the most recent articles.
- The script then prints these titles to the console.
- In case of any errors during the API request, appropriate error messages are displayed.

## Usage

You can use this script to quickly fetch and display the titles of the latest articles on English Wikipedia. It's a handy tool for staying updated with recent changes and trending topics on the platform.

## Requirements

- Python
- The `requests` library (installable via `pip install requests`)

## Note

Make sure to use this script responsibly and in compliance with Wikipedia's API usage policies. Respect rate limits and any terms of use specified by Wikipedia.
