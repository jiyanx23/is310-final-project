# Rework code for notebook assignment

# Step 0: Import libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_webpage(url): #rename function to be more meaningful
    response = requests.get(url)

    html_string = response.text
    return html_string

# Step 1: Create a function for getting the urls wuth title

#lowercase and underscores are the normal convention for naming functions in Python. Camelcasing like you had is more normal in JavaScript or for classes.
def get_content(url, keyword, url_head):
    content = scrape_webpage(url)
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('a')

    # linkList = []
    # volumeList = [] #Save yourself having to zip your lists by just creating your dictionary from the ouset
    result = {} #Create a dictionary to store the results, and give a more descriptive name to the variable
    for link in links:
        text = link.get_text().lower()
        if keyword in text:
            result[text] = url_head + link.get('href')

    # res = dict(zip(volumeList, linkList))

    # Saving into new py doc

    # with open(filename, 'w') as file:
    #     file.write(json.dumps(result, indent=2))

    return result


def scraping(links):
    data_list = []
    for key, value in links.items():
        data_dictionary = {}
        metadata_date = key.split(".")[1]
        data_dictionary["dates"] = metadata_date
        # print(f"{key}    {value}")
        content = scrape_webpage(value)
        soup = BeautifulSoup(content, "html.parser")
        data = soup.get_text()
        data_dictionary["text"] = data
        data_dictionary["url"] = value
        data_list.append(data_dictionary)
    return data_list

def main():
    res = get_content(url="https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/",keyword="humanist",url_head="https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/")

    content_dic = scraping(res)
    humanist_vols = pd.DataFrame.from_records(content_dic,columns=['dates','text','url'])

    humanist_vols.to_csv('web_scraped_humanist_listserv.csv', index=False)

   

        
main()