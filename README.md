# Space Instagram

Python3 project that can perform following things:
1. Download photos from Hubble public galleries
2. Download photos from SpaceX latest launch
3. Upload pictures to your Instagram account

## How to install

1. Register on [instagram.com](https://www.instagram.com/) (it is safer to create a new account).
3. Create file ```.env``` in the directory with this script and put there your instagram login, password and path to directory where you would like to keep your photos. ```.env``` file should look like this
```
LOGIN=space_cadet
PASSWORD=password228
DIRECTORY=images/
```
but with your data instead of presented above (you can keep DIRECTORY parameter as it is).

4. Python3 should be already installed. The script was made using `Python 3.7.3`. This version or higher should be fine.

5. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## How to use

First of all, you want to get some space photos. You can achieve this with one of the following comands (or both).
```
$ python3 fetch_spacex.py
```
```
$ python3 fetch_hubble.py
```
Then you would like to upload them to your Instagram account
```
$ python3 instabot_post.py 
2019-07-14 18:54:37,124 - INFO - Instabot Started
2019-07-14 18:54:37,125 - INFO - Logged-in successfully as 'space_cadet' using the cookie!
2019-07-14 18:55:08,817 - INFO - Photo 'images/resized/hubble3901_resized.jpg' is uploaded.
2019-07-14 18:55:32,635 - INFO - Photo 'images/resized/hubble3907_resized.jpg' is uploaded.
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
