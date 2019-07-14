import os
import requests
import urllib3

from dotenv import load_dotenv

from utility import download_photo, get_file_ext


def get_hubble_collection(collection_name):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url, params={'page': 'all'})
    collection_data = response.json()
    photos_ids = []
    for item in collection_data:
        photos_ids.append(item['id'])
    return photos_ids


def fetch_hubble_photo(photo_id, directory='images/'):
    url = f'http://hubblesite.org/api/v3/image/{photo_id}'
    response = requests.get(url)
    photo_data = response.json()['image_files'][-1]
    photo_url = 'https:' + photo_data['file_url']
    photo_ext = get_file_ext(photo_url)
    path_to_file = directory + f'hubble{photo_id}.{photo_ext}'
    download_photo(photo_url, path_to_file)


if __name__ == '__main__':
    load_dotenv()
    directory = os.getenv('DIRECTORY')
    os.makedirs(directory, exist_ok=True)
    urllib3.disable_warnings()

    collection_name = 'printshop'
    collection_photos_ids = get_hubble_collection(collection_name)
    for photo_id in collection_photos_ids:
        fetch_hubble_photo(photo_id, directory=directory)
        print(f'photo #{photo_id} downloaded.')
