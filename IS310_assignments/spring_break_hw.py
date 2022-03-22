from bs4 import BeautifulSoup
import requests



infile = open("raw_script_urls.txt", "r", encoding = "ISO-8859-1")
urls = []
website_name = []
for line in infile:
    # index = line.strip().find("http")
    # url = line.strip()[index:]
    line_split = line.strip().split(" +++$+++ ")
    urls.append(line_split[2])
    website_name.append(line_split[1])
    # urls.append(url)


for i in range(len(urls)):
    try:
        response = requests.get(urls[i])
    except requests.ConnectionError:
        print("connection error")      
    else:
        response_text = response.text
        soup = BeautifulSoup(response_text, features="html.parser") 
        script = soup.find('pre')
        if not type(script) == type(None):
            outfile = open(f"{website_name[i]}.txt", "w")
            outfile.write(script.get_text())
    


infile.close()
outfile.close()


