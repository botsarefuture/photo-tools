import os
from config import (PHOTO_FORMATS, IMAGES, VIDEO1_FORMATS, VIDEOS, DIRS_PATH)
def calculate_aspect(width: int, height: int) -> str:
    temp = 0

    def gcd(a, b):
        """The GCD (greatest common divisor) is the highest number that evenly divides both width and height."""
        return a if b == 0 else gcd(b, a % b)

    if width == height:
        return "1:1"

    if width < height:
        temp = width
        width = height
        height = temp


    divisor = gcd(width, height)

    x = int(width / divisor) if not temp else int(height / divisor)
    y = int(height / divisor) if not temp else int(width / divisor)

    return x, y
print(calculate_aspect(1080, 1920)) # '16:9')

def suunta(DIRS_PATH, format_suunta, make_dire, date_path, y, x, suunta_path):
    if not os.path.exists(DIRS_PATH + date_path + suunta_path):
        os.mkdir(DIRS_PATH + date_path + suunta_path)
    if y == 720:
        suunta_path += "/720p"
    elif y == 1080 and x == 1920 or x == 1080 and x == 1920:
        suunta_path += "/1080p"
    elif y == 1080 and x == 2048 or x == 1080 and y == 2048:
        suunta_path += "/2k"
    elif y == 2160 and x == 3840 or x == 2160 and y == 3840:
        suunta_path += "/4k"
    else:
        suunta_path = f"/{y}"
    return suunta_path

def format_date(day, month, year):
    return f"{day}.{month}.{year}"


def date(text):
    year = text[0:4]
    month = text[5:7]
    day = text[8:10]
    return day, month, year

def get_photos(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            for format in PHOTO_FORMATS:
                if f.lower().endswith(format):
                    IMAGES.append(os.path.join(root, f))
            for format in VIDEO1_FORMATS:
                if f.lower().endswith(format):
                    VIDEOS.append(os.path.join(root, f))

def suunta_maaritus(date_path, y, x):
    if y < x:
        suunta_path = suunta(DIRS_PATH, date_path, y, x, "vaaka")

    elif x < y:
        suunta_path = suunta(DIRS_PATH, date_path, y, x, "pysty")
            
    elif x == y or x-1==y or y-1==x:
        suunta_path = suunta(DIRS_PATH, date_path, y, x, "nelio")
    return suunta_path