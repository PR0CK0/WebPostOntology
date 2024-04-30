import requests
from bs4 import BeautifulSoup
import os

###################################

scriptDir = os.path.dirname(os.path.abspath(__file__))
outputPath = scriptDir

###################################

odng1 = 'https://www.orlandodatenightguide.com/post-sitemap.xml'
odng2 = 'https://www.orlandodatenightguide.com/post-sitemap2.xml'
odng3 = 'https://www.orlandodatenightguide.com/post-sitemap3.xml'

op1 = 'https://orlando-parenting.com/post-sitemap.xml'

tbp1 = 'https://tampabayparenting.com/post-sitemap1.xml'
tbp2 = 'https://tampabayparenting.com/post-sitemap2.xml'
tbp3 = 'https://tampabayparenting.com/post-sitemap3.xml'
tbp4 = 'https://tampabayparenting.com/post-sitemap4.xml'
tbp5 = 'https://tampabayparenting.com/post-sitemap5.xml'

tbdng1 = 'https://tampabaydatenightguide.com/post-sitemap.xml'

###################################

urls = [odng1, odng2, odng3, op1, tbp1, tbp2, tbp3, tbp4, tbp5, tbdng1]

###################################

url_to_file = {
    odng1: 'odng1.txt',
    odng2: 'odng2.txt',
    odng3: 'odng3.txt',
    op1: 'op1.txt',
    tbp1: 'tbp1.txt',
    tbp2: 'tbp2.txt',
    tbp3: 'tbp3.txt',
    tbp4: 'tbp4.txt',
    tbp5: 'tbp5.txt',
    tbdng1: 'tbdng1.txt'
}

for url, filename in url_to_file.items():
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml-xml')
        loc_elements = soup.find_all('loc')

        with open(outputPath + '/' + filename, 'w') as file:
            file.write(f"URL: {url}\n")

            for loc in loc_elements[1:]:
                loc_text = loc.get_text()
                if loc_text.endswith('/'):
                    file.write(f"{loc_text}\n")

    else:
        with open(filename, 'w') as file:
            file.write(f"Failed to retrieve {url}. Status code: {response.status_code}\n\n\n")