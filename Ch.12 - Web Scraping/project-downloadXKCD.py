# Download all XKCD comics

import requests
import os
import bs4

url = 'https://xkcd.com'

# Create a folder to store comics
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find comic strip URL
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print("Could not find comic image")
    else:
        comicURL = 'https:' + comicElem[0].get('src')

        # Download image
        print(f"Downloading image {comicURL}")
        res = requests.get(comicURL)
        res.raise_for_status()

    # Save image
    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')

    for chunk in res.iter_content(10000):
        imageFile.write(chunk)

    imageFile.close()

    # Get prev button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done!')
