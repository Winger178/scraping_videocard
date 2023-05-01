from bs4 import BeautifulSoup
import requests
import json

#data_source
url = 'https://technical.city/ru/video/rating'

#for_ystem_trust
headers = {
    'Accept': '*/*',
    'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}

#request_from_data_source_&_writing_file
req = requests.get(url, headers=headers)
output = req.text


with open('index.html', 'w', encoding='utf-8') as file:
    file.write(output)

#read_html_file
with open('index.html', 'r', encoding='utf-8') as file:
    src = file.read()

#search_data_table
soup = BeautifulSoup(src, 'lxml')

table = soup.find_all('tr')

all_objects = {}
num = 0
massive = ['\n', '\t']

#data_sorting
for i in table:
    exp = []
    for j in i:
        if (str(j.text) != '\n') and not(str(j.text).isdigit()) and (str(j.text) != '№ ') and (str(j.text) != ''):

            exp.append(str(j.text).replace('\n', '').replace('\t', ''))

    if len(exp) > 3:
        all_objects[num] = exp
        num += 1



#rewriting_in_json
with open('answer.json', 'w', encoding='utf-8') as f:
    json.dump(all_objects, f, indent=4, ensure_ascii=False)

