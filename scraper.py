import requests
import shutil
import bs4
import os

MAIN_URL = 'https://namemc.com/'
SKINS_URL = MAIN_URL + 'minecraft-skins/trending/daily?page={}'
DOWNLOAD_URL = MAIN_URL + 'texture/{}'
CURR_PATH = os.path.dirname(os.path.realpath(__file__))


def download_skin(skin_code):
    """
    Function takes a skin code of the selected
    skin and downloads it to the Skins Folder.

    :param skin_code: the skin's code in the site
    :type skin_code: str

    :return: None
    """
    img_url = DOWNLOAD_URL.format(skin_code) + '.png'
    print(img_url)
    img_url = requests.get(img_url, stream=True)

    path = CURR_PATH + "\\Skins\\{}".format(skin_code) + '.png'
    with open(path, 'wb') as f:
        shutil.copyfileobj(img_url.raw, f)


def main():
    if os.path.isdir(CURR_PATH + '\\Skins\\'):
        print("---Directory Exists !---\nPress Ctrl+C to Stop!\n")
    else:
        os.mkdir("Skins")
        print("---Direcory Created---\n\tPress Ctrl+C to Stop!\n")

    for i in range(1, 68):
        working = SKINS_URL.format(str(i))
        working = requests.get(working).text

        soup = bs4.BeautifulSoup(working, 'lxml')
        for skin in soup.find_all('a', href=True):
            try:
                href_ = skin.get('href')
                if '/skin/' in href_:
                    download_skin(href_[href_.index('n/') + 2:])
            except KeyboardInterrupt:
                print("\nStopped!")



if __name__ == "__main__":
    main()
