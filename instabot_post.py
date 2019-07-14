import os
import shutil
from os.path import isfile
from os.path import join as joinpath
from time import sleep

from instabot import Bot
from dotenv import load_dotenv

from image_processing import process_image


if __name__ == '__main__':
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    directory = os.getenv('DIRECTORY')
    posted_directory = joinpath(directory, 'posted')
    os.makedirs(posted_directory, exist_ok=True)

    bot = Bot()
    bot.login(username=login, password=password)

    photos = os.listdir(directory)
    for photo in photos:
        path = joinpath(directory, photo)
        if isfile(path):
            photo_path = path
            # It is not a feature. It is necessity.
            new_photo_path = process_image(photo_path)
            bot.upload_photo(new_photo_path)
            shutil.move(photo_path, joinpath(posted_directory, photo))
            sleep(20)
