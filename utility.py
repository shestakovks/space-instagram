import requests


def get_file_ext(url):
    return url.split('.')[-1]


def download_photo(url, path_to_file):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path_to_file, 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    # bad url
    url = 'https://api.spacexdata.com/v3/launches/latestz'
    path = 'images/test.jpg'
    try:
        download_photo(url, path)
    except requests.exceptions.HTTPError:
        print('Something went completely wrong.')
