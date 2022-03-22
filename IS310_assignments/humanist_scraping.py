from base64 import urlsafe_b64decode
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

# for k, v in volume_links.items():
#     print(k)


sub_links = {}

for key, value in volume_links.items():
    link_sub = {}
    response_sub = requests.get(value)
    response_text_sub = response_sub.text
    soup_sub = BeautifulSoup(response_text_sub, features="html.parser")
    links_sub = soup_sub.find_all('a')
    for links in links_sub:
        text_sub = links.get_text()
        url_sub = links.get("href")
        # print(url_sub)
        if "subject.html" in response_sub.url:
            index = response_sub.url.find("subject.html")
            new_url = response_sub.url[:index]
            link_sub[text_sub] = f"{new_url}{url_sub}"
            # print(f"{new_url}{url_sub}")
        else:
            link_sub[text_sub] = f"{value}{url_sub}"
    sub_links[key] = link_sub

# from this part is the getting two website content
# for k,v in sub_links.items():
#     print(k)

volume1_url = sub_links["Volume 1 5/87-5/88"]["8705.1324.txt"]    
volume1_reponse = requests.get(volume1_url)
response_text_1 = volume1_reponse.text
soup_1 = BeautifulSoup(response_text_1, features="html.parser")
volume1_text = soup_1.getText()
# print(soup_1.get_text())


volume33_url = sub_links["Volume 33"]["May 7, 2019, 6:16 a.m. Humanist 33.1"]
volume33_reponse = requests.get(volume33_url)
response_text_33 = volume33_reponse.text
soup_33 = BeautifulSoup(response_text_33, features="html.parser")
volume33_text = soup_33.getText()
# print(soup_33.get_text())











# volume31 = volume_links["Volume 31"]
# volume32 = volume_links["Volume 32"]
# volume31_response = requests.get(volume31)
# volume32_response = requests.get(volume32)
# soup_31 = BeautifulSoup(volume31_response.text, features="html.parser")
# soup_32 = BeautifulSoup(volume32_response.text, features="html.parser")
# print(soup_31.prettify())
# print(soup_32.prettify())


# response = requests.get("https://humanist.kdl.kcl.ac.uk/")

# print(response.status_code)
# print(response.headers)