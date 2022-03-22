from bs4 import BeautifulSoup
import requests

website = "https://humanist.kdl.kcl.ac.uk/"

response = requests.get(website)
response_text = response.text
soup = BeautifulSoup(response_text, features="html.parser")
# print(soup.prettify())


links = soup.find_all('a')

volume_links = {}

for link in links:
    text = link.get_text()
    url = link.get("href")
    if "Volume" in text:
        # print(url)
        
        volume_links[text] = f"{website}{url[1:]}"
        # print(volume_links[text])

volume31 = volume_links["Volume 31"]
volume32 = volume_links["Volume 32"]
volume31_response = requests.get(volume31)
volume32_response = requests.get(volume32)
soup_31 = BeautifulSoup(volume31_response.text, features="html.parser")
soup_32 = BeautifulSoup(volume32_response.text, features="html.parser")
# print(soup_31.prettify())
# print(soup_32.prettify())


# response = requests.get("https://humanist.kdl.kcl.ac.uk/")

# print(response.status_code)
# print(response.headers)