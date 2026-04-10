import requests
from bs4 import BeautifulSoup

"""
Google Docs Secret Message Decoder
This script scrapes a published Google Doc table containing (x, character, y) 
coordinates and reconstructs the intended visual message in the terminal.
"""

def write(url):
    # Fetch the HTML content from the published Google Doc
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Could not retrieve the document.")
        return

    # Parse the HTML to locate the data table
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    
    # Remove the header row (e.g., "x-coordinate", "Character", "y-coordinate")
    # so it doesn't interfere with integer conversion later
    firstRow = table.find("tr")
    if firstRow:
        firstRow.decompose()

    # Extract raw text from each table cell and store as a list of lists
    data = []
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        data.append([cell.get_text(strip=True) for cell in cells])

    # Convert coordinate strings into integers for mathematical sorting
    for d in data:
        d[0] = int(d[0])  # x-coordinate
        d[2] = int(d[2])  # y-coordinate

    # Sort data: Primary sort by Y (top to bottom), 
    # Secondary sort by X (left to right)
    # Note: reverse=True handles the grid if the Doc uses a bottom-up Y axis
    data.sort(key=lambda row: (row[2], -row[0]), reverse=True)

    # Track positioning to handle line breaks and spaces
    prevY = None
    prevX = -1

    for d in data:
        # If the Y-coordinate changes, move to a new line in the terminal
        if d[2] != prevY and prevY is not None:
            print()
            print(d[1], end="")
        
        # If there is a gap between the current and previous X-coordinate,
        # print spaces to maintain the visual structure
        elif d[0] != prevX + 1:
            for i in range(d[0] - prevX):
                print(" ", end="")
        
        # Otherwise, just print the character on the same line
        else:
            print(d[1], end="")

        # Update trackers for the next iteration
        prevY = d[2]
        prevX = d[0]

if __name__ == "__main__":
    # Target URL (Published Google Doc)
    url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    write(url)
