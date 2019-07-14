import requests


def get_file_ext(url):
    return url.split('.')[-1]


def download_photo(url, path_to_file):
    response = requests.get(url, verify=False)
    with open(path_to_file, 'wb') as f:
        f.write(response.content)
