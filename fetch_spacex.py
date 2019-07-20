import os
import requests
import urllib3

from dotenv import load_dotenv

from utility import download_photo, get_file_ext


def fetch_spacex_last_launch(directory='images/'):
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    photos_urls = response.json()['links']['flickr_images']
    for num, url in enumerate(photos_urls):
        photo_ext = get_file_ext(url)
        path_to_file = f'{directory}spacex{num+1}.{photo_ext}'
        download_photo(url, path_to_file)
        print(f'photo #{num+1} downloaded.')


if __name__ == '__main__':
    load_dotenv()
    directory = os.getenv('DIRECTORY')
    os.makedirs(directory, exist_ok=True)
    urllib3.disable_warnings()
    try:
        fetch_spacex_last_launch(directory=directory)
    except requests.exceptions.HTTPError:
        print('Something went wrong.')
