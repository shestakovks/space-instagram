import os
import os.path

from PIL import Image


def get_new_path(path_to_file):
    head, tail = os.path.split(path_to_file)
    root, ext = os.path.splitext(tail)
    path_to_new_file = f'{head}/resized/{root}_resized{ext}'
    return path_to_new_file


def save_image(image, path_to_file):
    head, _ = os.path.split(path_to_file)
    os.makedirs(head, exist_ok=True)
    image.save(path_to_file)


def resize_horizontal(image, max_width=1080):
    ratio = max_width / image.width
    new_width = int(image.width * ratio)
    new_height = int(image.height * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def resize_vertical(image, max_height=1350):
    new_image = resize_horizontal(image)
    if new_image.height <= max_height:
        return new_image
    delta_height = new_image.height - max_height
    crop_step = delta_height / 2
    crop_box = (
        0,  # left
        crop_step,  # upper
        new_image.width,  # right
        new_image.height - crop_step  # lower
    )
    cropped_image = new_image.crop(crop_box)
    return cropped_image


def process_image(path_to_file, max_width=1080, max_height=1350):
    image = Image.open(path_to_file)
    if image.width <= max_width and image.height <= max_height:
        return path_to_file
    if image.width > image.height:
        new_image = resize_horizontal(image)
    else:
        new_image = resize_vertical(image)
    new_path = get_new_path(path_to_file)
    save_image(new_image, new_path)
    return new_path


if __name__ == '__main__':
    pass
