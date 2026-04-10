import requests
from bs4 import BeautifulSoup
"""

https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub
https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub
"""
def write(url):


    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first table on the page
    table = soup.find("table")
    firstRow = table.find("tr")
    firstRow.decompose()
    data = []
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        data.append([cell.get_text(strip=True) for cell in cells])

    for d in data:
        d[0] = int(d[0])
        d[2] = int(d[2])

    data.sort(key=lambda row: (row[2], -row[0]), reverse=True)
    prevY = None
    prevX = - 1

    for d in data:
        if d[2] != prevY and prevY is not None:
            print()
            print(d[1], end="")
        elif d[0] != prevX + 1:
            for i in range(d[0]-prevX):
                print(" ", end="")
        else:
            print(d[1], end="")

        prevY = d[2]
        prevX = d[0]
if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    write(url)

