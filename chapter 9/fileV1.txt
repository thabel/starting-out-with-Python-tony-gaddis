import requests
from bs4 import BeautifulSoup
import json

# continue here https://beautiful-soup-4.readthedocs.io/en/latest/#going-sideways

url = 'https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210'


def main():
    capitals = {}
    response_url = requests.get(url)
    # print(response_url.content)
    soup = BeautifulSoup(response_url.content, 'html.parser')
    table_tag = soup.find('table')
    for tag in table_tag.find_all('tr')[1:]:
        key, value = tag.contents[:2]
        capitals[str(key.string)] = str(value.string)
    with open("UsaCapitales.json", "w") as f:
        f.write(json.dumps(capitals, indent=4))


if __name__ == '__main__':
    main()
