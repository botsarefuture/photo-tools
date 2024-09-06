import os
from config import PHOTO_FORMATS, IMAGES, VIDEO1_FORMATS, VIDEOS, DIRS_PATH

def calculate_aspect(width: int, height: int) -> str:
    """Calculate the aspect ratio of the given width and height."""
    
    def gcd(a, b):
        """Calculate the Greatest Common Divisor (GCD) of a and b."""
        while b:
            a, b = b, a % b
        return a

    if width == height:
        return "1:1"

    if width < height:
        width, height = height, width

    divisor = gcd(width, height)
    x = width // divisor
    y = height // divisor

    return f"{x}:{y}"

print(calculate_aspect(1080, 1920))  # Expected output: '16:9'

def get_suunta_path(DIRS_PATH: str, date_path: str, y: int, x: int) -> str:
    """Determine the subdirectory path based on resolution."""
    suunta_path = ""

    if y == 720:
        suunta_path = "/720p"
    elif (y == 1080 and x == 1920) or (x == 1080 and y == 1920):
        suunta_path = "/1080p"
    elif (y == 1080 and x == 2048) or (x == 1080 and y == 2048):
        suunta_path = "/2k"
    elif (y == 2160 and x == 3840) or (x == 2160 and y == 3840):
        suunta_path = "/4k"
    else:
        suunta_path = f"/{y}"

    full_path = os.path.join(DIRS_PATH, date_path, suunta_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return suunta_path

def format_date(day: str, month: str, year: str) -> str:
    """Format the date in the format day.month.year."""
    return f"{day}.{month}.{year}"

def parse_date(text: str) -> tuple:
    """Extract day, month, and year from a date string."""
    year = text[:4]
    month = text[5:7]
    day = text[8:10]
    return day, month, year

def get_photos(path: str):
    """Scan directory for photo and video files based on configured formats."""
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file).lower()
            if any(file_path.endswith(fmt) for fmt in PHOTO_FORMATS):
                IMAGES.append(file_path)
            if any(file_path.endswith(fmt) for fmt in VIDEO1_FORMATS):
                VIDEOS.append(file_path)

def determine_suunta(date_path: str, y: int, x: int) -> str:
    """Determine the direction (landscape/portrait/square) based on resolution."""
    if y < x:
        return get_suunta_path(DIRS_PATH, date_path, y, x)
    elif x < y:
        return get_suunta_path(DIRS_PATH, date_path, y, x)
    else:
        return get_suunta_path(DIRS_PATH, date_path, y, x)

