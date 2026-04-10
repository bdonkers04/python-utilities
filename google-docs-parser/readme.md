# 🧩 Google Docs Grid Decoder

A Python-based technical utility that scrapes coordinate-based character data from published Google Docs and reconstructs them into a visual grid message.

## 📖 The Challenge
The input data is stored in a published Google Doc table with three columns: `x-coordinate`, `character`, and `y-coordinate`. The data is often provided in a random order. This tool parses the HTML, sorts the coordinates, and handles the spatial gaps to reveal the hidden message.

## 🚀 Features
* **Web Scraping:** Uses `BeautifulSoup4` and `Requests` to extract data directly from live Google Doc URLs.
* **Coordinate Mapping:** Implements a custom sorting algorithm using Python lambdas to order data by Y and X axes.
* **Spatial Reconstruction:** Dynamically calculates gaps between coordinates to inject the correct number of spaces and line breaks for terminal output.

## 🛠️ Requirements
This project requires two industry-standard Python libraries:
```bash
pip install requests beautifulsoup4
