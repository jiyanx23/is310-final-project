from bs4 import BeautifulSoup
import requests



infile = open("raw_script_urls.txt", "r", encoding = "ISO-8859-1")
outfile = open("scripts.txt", "w")
urls = []
for line in infile:
    index = line.strip().find("http")
    url = line.strip()[index:]
    # print(url)
    urls.append(url)

# url = urls[0]
# response = requests.get(url)
# response_text = response.text
# soup = BeautifulSoup(response_text, features="html.parser") 
# script = soup.find_all('pre')
# print(script)

for url in urls:
    response = requests.get(url)
    response_text = response.text
    soup = BeautifulSoup(response_text, features="html.parser") 
    script = soup.find('pre').get_text()
    outfile.write(script)


infile.close()
outfile.close()


