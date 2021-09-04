# Download all XKCD comics

import requests
import os
import bs4
import threading

# Create a folder to store comics
os.makedirs('xkcd', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download page
        print(f'Downloading page https://xkcd.com/{urlNumber}...')
        res = requests.get(f'https://xkcd.com/{urlNumber}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find comic strip URL
        comicElem = soup.select('#comic img')

        if comicElem == []:
            print("Could not find comic image")
        else:
            comicURL = comicElem[0].get('src')

            # Download image
            print(f"Downloading image {comicURL}")
            res = requests.get(f'https://{comicURL}')
            res.raise_for_status()

            # Save image
            imageFile = open(os.path.join(
                'xkcd', os.path.basename(comicURL)), 'wb')

            for chunk in res.iter_content(10000):
                imageFile.write(chunk)

            imageFile.close()


# List of threads
downloadThreads = []

# Creates 14 threads, each one downloading 10 comics
for i in range(0, 140, 10):
    start = i
    end = i + 9

    # There's no comic 0, so set to 1
    if i == 0:
        start = 1

    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to finish
# The .join method waits for the thread to finish before continuing in the code. This FOR loop
# Means that we wait for all threads to finish before continuing
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done!')
