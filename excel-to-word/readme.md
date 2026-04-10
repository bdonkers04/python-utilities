# Excel-to-Word Report Automator

A specialized Python utility designed to migrate structured tabular data and embedded imagery from Microsoft Excel (.xlsx) into formatted Microsoft Word (.docx) documents.

## Business Case
In many administrative and technical workflows, data is collected in spreadsheets but must be presented in a formal document format. Manually migrating this data—especially images—is time-consuming and prone to human error. This script automates that bridge.

## Technical Features
* **Dynamic Table Generation:** Automatically calculates the grid dimensions (`max_row` and `max_column`) to ensure the Word table perfectly matches the source Excel layout.
* **Binary Image Extraction:** Accesses the "hidden" `_images` attribute in `openpyxl` to extract, temporarily buffer, and re-insert graphical assets into the final report.
* **Resource Management:** Implements automated cleanup of temporary image files to ensure a zero-footprint execution on the host machine.

## Requirements
You will need the following Python libraries:
```bash
pip install openpyxl python-docx
