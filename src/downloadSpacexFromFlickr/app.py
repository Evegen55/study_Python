import os.path
import re
import urllib.request
from os.path import expanduser

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.8'
}

home = expanduser("~")


def read_file(filename):
    with open(filename) as input_file:
        text1 = input_file.read()
    return text1


def downloadPhotoToHomeFolder(url_done_download, username, cleared):
    directory = home + '\\' + 'Downloads\\' + username
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print(directory, ' exists')

    file_out = directory + '\\' + cleared + '.jpg'
    if not os.path.exists(file_out):
        print('Downloading image: ', url_done_download)
        urllib.request.urlretrieve(url_done_download, file_out)
    pass


def processPhotoStreamFile(file_out, cleared, username):
    print(f'Finding the biggest file in file {file_out}')
    text = read_file(file_out)
    displayUrls = re.findall('"o":.*{"displayUrl.*"}', text)
    if len(displayUrls) == 0:
        displayUrls = re.findall('"k":.*{"displayUrl.*"}', text)
    displayUrl = displayUrls[0]
    # pat = 'farm1.staticflickr.com.*' + str(cleared) + '_.*.jpg","w'
    pat = 'farm[0-9].staticflickr.com.*' + '_.*.jpg","w'
    print('pattern is: ', pat)
    url_searched_list = re.findall(pat, displayUrl)
    if len(url_searched_list) == 0:
        print("empty file???")
    url_searched = url_searched_list[0]
    # lenght = len(url_searched) - 4
    lenght = 58
    url_searched_cleared = url_searched[0:lenght]
    url_done = 'http://' + url_searched_cleared.replace('\/', '/')
    url_done_download = 'http://' + url_searched_cleared.replace('\/', '/').replace('_o', '_o_d')
    print(url_done)
    print(url_done_download)
    downloadPhotoToHomeFolder(url_done_download, username, cleared)


pass


def goToPhotoStreamPageAndDownloadTheBiggestImage(photostreamURL, cleared, username):
    directory = home + '\\' + 'Downloads\\' + username + '\\' + 'pages'
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print(directory, ' exists')

    file_out = f'{directory}/{cleared}.html'

    if not os.path.exists(file_out):
        print('Process photostream url: ', photostreamURL)
        r = requests.get(photostreamURL, headers)
        with open(file_out, 'w') as output_file:
            output_file.write(r.text.encode('utf-16'))

    processPhotoStreamFile(file_out, cleared, username)
    pass


def scan_user(username, num_pages):
    '''
    Parse first start page, get list of photostream's pages and download all biggest images
    :param username:
    :param num_pages:
    :return:
    '''
    base_url = 'https://www.flickr.com/photos/%s' % username
    for page_number in range(num_pages):
        page_number = page_number + 1
        url = base_url + '/page%d' % page_number  # download page to a file

        directory_username = home + '\\' + 'Downloads\\' + username
        if not os.path.exists(directory_username):
            os.makedirs(directory_username)
        else:
            print(directory_username, ' exists')

        file_out = f'{directory_username}/page{page_number}.html'

        if not os.path.exists(file_out):
            print('Process main url: ', url)
            r = requests.get(url, headers)
            with open(file_out, 'w') as output_file:
                output_file.write(r.text)

        text = read_file(file_out)

        # Beautiful Soup
        soup = BeautifulSoup(text, "lxml")
        div_list = soup.find('div', {'class': "view photo-list-view requiredToShowOnServer photostream"})
        items = div_list.find_all('div',
                                  {'class': 'view photo-list-photo-view requiredToShowOnServer photostream awake'})

        for item in items:
            style = item.get('style')
            # c1.staticflickr.com/1/799/27684194488_b4b1b95c88_n.jpg
            background_image = re.findall("c1.staticflickr.com.*.jpg", style)[0]
            num_image = re.findall("/[0-9]*_", background_image)[0]  # /27684194488_
            lenght = len(num_image) - 1
            num_image_cleared = num_image[1:lenght]  # 27684194488
            photostreamURL = f'https://www.flickr.com/photos/{username}/{num_image_cleared}/in/photostream/'
            # print(background_image, ' ', num_image, num_image_cleared, photostreamURL)
            goToPhotoStreamPageAndDownloadTheBiggestImage(photostreamURL, num_image_cleared, username)


# test
username1 = 'spacex'
num_pages1 = 7

username2 = 'ming_chai'
num_pages2 = 1
scan_user(username2, num_pages2)
